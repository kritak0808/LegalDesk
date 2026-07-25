import uuid
from typing import List, Optional, Dict, Any
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.litigation import LitigationCase
from app.core.exceptions import NotFoundException, ValidationException


class LitigationService:
    VALID_STATUSES = [
        "Case Intake", "Conflict Check", "Investigation", "Legal Research",
        "Evidence Collection", "Discovery", "Pre-Trial", "Trial", "Judgment",
        "Appeal", "Settlement", "Closed", "Archived"
    ]

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_case_by_id(self, case_id: str, organization_id: str) -> LitigationCase:
        stmt = select(LitigationCase).where(
            LitigationCase.id == case_id,
            LitigationCase.organization_id == organization_id,
            LitigationCase.is_deleted == False
        )
        case = (await self.db.execute(stmt)).scalars().first()
        if not case:
            raise NotFoundException("LitigationCase", case_id)
        return case

    async def transition_status(self, case_id: str, organization_id: str, new_status: str) -> LitigationCase:
        if new_status not in self.VALID_STATUSES:
            raise ValidationException(f"Invalid status '{new_status}'. Allowed: {', '.join(self.VALID_STATUSES)}")

        case = await self.get_case_by_id(case_id, organization_id)
        case.status = new_status
        await self.db.flush()
        return case
