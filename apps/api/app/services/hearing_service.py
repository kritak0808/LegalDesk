from typing import List
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.litigation import Hearing


class HearingService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_case_hearings(self, case_id: str) -> List[Hearing]:
        stmt = select(Hearing).where(Hearing.case_id == case_id).order_by(Hearing.scheduled_at.asc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
