from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.matter import Matter


class MatterSearchService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def search_matters(
        self,
        organization_id: str,
        query: Optional[str] = None,
        category_id: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        risk_level: Optional[str] = None,
        jurisdiction: Optional[str] = None,
        skip: int = 0,
        limit: int = 50
    ) -> List[Matter]:
        stmt = select(Matter).where(Matter.organization_id == organization_id, Matter.is_deleted == False)

        if query:
            stmt = stmt.where(
                (Matter.title.ilike(f"%{query}%")) |
                (Matter.matter_number.ilike(f"%{query}%")) |
                (Matter.description.ilike(f"%{query}%"))
            )
        if category_id:
            stmt = stmt.where(Matter.category_id == category_id)
        if status:
            stmt = stmt.where(Matter.status == status)
        if priority:
            stmt = stmt.where(Matter.priority == priority)
        if risk_level:
            stmt = stmt.where(Matter.risk_level == risk_level)
        if jurisdiction:
            stmt = stmt.where(Matter.jurisdiction == jurisdiction)

        stmt = stmt.order_by(Matter.updated_at.desc()).offset(skip).limit(limit)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
