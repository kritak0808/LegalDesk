from typing import List, Optional, Dict, Any
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.matter import MatterTimeline


class MatterTimelineService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def log_event(
        self,
        matter_id: str,
        event_type: str,
        title: str,
        description: Optional[str] = None,
        created_by_id: Optional[str] = None,
        metadata_json: Optional[Dict[str, Any]] = None
    ) -> MatterTimeline:
        event = MatterTimeline(
            matter_id=matter_id,
            event_type=event_type,
            title=title,
            description=description,
            created_by_id=created_by_id,
            metadata_json=metadata_json or {}
        )
        self.db.add(event)
        await self.db.flush()
        return event

    async def get_timeline(self, matter_id: str) -> List[MatterTimeline]:
        stmt = select(MatterTimeline).where(MatterTimeline.matter_id == matter_id).order_by(MatterTimeline.created_at.desc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
