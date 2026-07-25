import uuid
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.matter import Matter, MatterCategory, MatterParticipant, MatterActivity
from app.core.exceptions import NotFoundException, ValidationException


class MatterService:
    VALID_STATUSES = [
        "Draft", "Intake", "Assigned", "Under Review", "Active",
        "Waiting", "Escalated", "Pending Approval", "Resolved",
        "Closed", "Archived", "Cancelled"
    ]

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_matter_by_id(self, matter_id: str, organization_id: str) -> Matter:
        stmt = select(Matter).where(
            Matter.id == matter_id,
            Matter.organization_id == organization_id,
            Matter.is_deleted == False
        )
        matter = (await self.db.execute(stmt)).scalars().first()
        if not matter:
            raise NotFoundException("Matter", matter_id)
        return matter

    async def get_matter_by_number(self, matter_number: str, organization_id: str) -> Matter:
        stmt = select(Matter).where(
            Matter.matter_number == matter_number,
            Matter.organization_id == organization_id,
            Matter.is_deleted == False
        )
        matter = (await self.db.execute(stmt)).scalars().first()
        if not matter:
            raise NotFoundException("Matter", matter_number)
        return matter

    async def transition_status(self, matter_id: str, organization_id: str, new_status: str, user_id: str) -> Matter:
        if new_status not in self.VALID_STATUSES:
            raise ValidationException(f"Invalid status '{new_status}'. Allowed: {', '.join(self.VALID_STATUSES)}")

        matter = await self.get_matter_by_id(matter_id, organization_id)
        old_status = matter.status
        matter.status = new_status

        if new_status in ["Resolved", "Closed"]:
            matter.closed_at = datetime.now(timezone.utc)

        # Log activity
        activity = MatterActivity(
            matter_id=matter.id,
            user_id=user_id,
            action="MATTER.STATUS_CHANGED",
            details_json={"from": old_status, "to": new_status}
        )
        self.db.add(activity)
        await self.db.flush()
        return matter
