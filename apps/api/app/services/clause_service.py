from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contract import ClauseLibrary, ClauseCategory


class ClauseService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_clauses(self, organization_id: str) -> List[ClauseLibrary]:
        stmt = select(ClauseLibrary).where(ClauseLibrary.organization_id == organization_id, ClauseLibrary.is_approved == True)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())

    async def list_categories(self, organization_id: str) -> List[ClauseCategory]:
        stmt = select(ClauseCategory).where(ClauseCategory.organization_id == organization_id)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
