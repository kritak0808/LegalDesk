from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.matter import MatterComment


class MatterCommentService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_comment(
        self,
        matter_id: str,
        user_id: str,
        content: str,
        parent_comment_id: Optional[str] = None,
        is_internal: bool = True
    ) -> MatterComment:
        comment = MatterComment(
            matter_id=matter_id,
            user_id=user_id,
            content=content,
            parent_comment_id=parent_comment_id,
            is_internal=is_internal,
            is_pinned=False,
            is_resolved=False
        )
        self.db.add(comment)
        await self.db.flush()
        return comment

    async def get_matter_comments(self, matter_id: str) -> List[MatterComment]:
        stmt = select(MatterComment).where(MatterComment.matter_id == matter_id).order_by(MatterComment.created_at.asc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
