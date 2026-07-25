import uuid
from datetime import datetime, timezone, timedelta
from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.invitation import Invitation
from app.core.exceptions import NotFoundException, ValidationException


class InvitationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_invitation(
        self,
        email: str,
        organization_id: str,
        invited_by_id: str,
        role_id: Optional[str] = None,
        user_type: str = "internal",
        expires_days: int = 7
    ) -> Invitation:
        # Check if pending invitation exists
        stmt = select(Invitation).where(
            Invitation.email == email,
            Invitation.organization_id == organization_id,
            Invitation.status == "pending"
        )
        existing = (await self.db.execute(stmt)).scalars().first()
        if existing:
            raise ValidationException(f"A pending invitation already exists for {email}.")

        token = f"inv_{uuid.uuid4().hex}"
        expires_at = datetime.now(timezone.utc) + timedelta(days=expires_days)

        inv = Invitation(
            email=email,
            token=token,
            organization_id=organization_id,
            role_id=role_id,
            invited_by_id=invited_by_id,
            user_type=user_type,
            expires_at=expires_at,
            status="pending"
        )
        self.db.add(inv)
        await self.db.flush()
        return inv

    async def get_invitations_by_org(self, organization_id: str) -> List[Invitation]:
        stmt = select(Invitation).where(Invitation.organization_id == organization_id).order_by(Invitation.created_at.desc())
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def verify_token(self, token: str) -> Invitation:
        stmt = select(Invitation).where(Invitation.token == token)
        inv = (await self.db.execute(stmt)).scalars().first()
        if not inv:
            raise NotFoundException("Invitation", token)
        if inv.status != "pending":
            raise ValidationException(f"Invitation has already been {inv.status}.")
        
        now = datetime.now(timezone.utc)
        expires_at = inv.expires_at.replace(tzinfo=timezone.utc) if inv.expires_at.tzinfo is None else inv.expires_at
        if now > expires_at:
            inv.status = "expired"
            await self.db.flush()
            raise ValidationException("Invitation has expired.")
            
        return inv

    async def revoke_invitation(self, invitation_id: str) -> bool:
        stmt = update(Invitation).where(Invitation.id == invitation_id).values(status="revoked")
        res = await self.db.execute(stmt)
        await self.db.flush()
        return res.rowcount > 0
