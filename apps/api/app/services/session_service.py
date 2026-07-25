import uuid
from datetime import datetime, timezone, timedelta
from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.session import UserSession
from app.core.exceptions import NotFoundException


class SessionService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_session(
        self,
        user_id: str,
        organization_id: Optional[str],
        ip_address: Optional[str] = "127.0.0.1",
        user_agent: Optional[str] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        device_type: str = "desktop",
        browser: str = "Chrome 122",
        os: str = "Windows 11",
        country: str = "United States"
    ) -> UserSession:
        token = f"sess_{uuid.uuid4().hex}"
        expires_at = datetime.now(timezone.utc) + timedelta(days=7)

        session_entry = UserSession(
            session_token=token,
            user_id=user_id,
            organization_id=organization_id,
            device_type=device_type,
            browser=browser,
            os=os,
            ip_address=ip_address,
            country=country,
            is_active=True,
            last_activity_at=datetime.now(timezone.utc),
            expires_at=expires_at,
        )
        self.db.add(session_entry)
        await self.db.flush()
        return session_entry

    async def get_user_sessions(self, user_id: str) -> List[UserSession]:
        result = await self.db.execute(
            select(UserSession)
            .where(UserSession.user_id == user_id, UserSession.is_active == True)
            .order_by(UserSession.last_activity_at.desc())
        )
        return list(result.scalars().all())

    async def revoke_session(self, session_id: str, user_id: str) -> bool:
        result = await self.db.execute(
            update(UserSession)
            .where(UserSession.id == session_id, UserSession.user_id == user_id)
            .values(is_active=False)
        )
        await self.db.flush()
        return result.rowcount > 0

    async def revoke_all_other_sessions(self, current_session_id: str, user_id: str) -> int:
        result = await self.db.execute(
            update(UserSession)
            .where(
                UserSession.user_id == user_id,
                UserSession.id != current_session_id,
                UserSession.is_active == True
            )
            .values(is_active=False)
        )
        await self.db.flush()
        return result.rowcount
