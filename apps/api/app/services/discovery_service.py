from typing import List
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.litigation import DiscoveryRequest


class DiscoveryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_discovery_requests(self, case_id: str) -> List[DiscoveryRequest]:
        stmt = select(DiscoveryRequest).where(DiscoveryRequest.case_id == case_id).order_by(DiscoveryRequest.due_date.asc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
