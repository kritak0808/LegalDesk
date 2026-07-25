from datetime import datetime
from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.matter import MatterTask
from app.core.exceptions import NotFoundException, ValidationException


class MatterTaskService:
    VALID_STATUSES = ["To Do", "In Progress", "In Review", "Completed", "Blocked"]

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_task(
        self,
        matter_id: str,
        title: str,
        description: Optional[str] = None,
        owner_id: Optional[str] = None,
        priority: str = "Medium",
        due_date: Optional[datetime] = None
    ) -> MatterTask:
        task = MatterTask(
            matter_id=matter_id,
            title=title,
            description=description,
            owner_id=owner_id,
            priority=priority,
            status="To Do",
            due_date=due_date
        )
        self.db.add(task)
        await self.db.flush()
        return task

    async def get_matter_tasks(self, matter_id: str) -> List[MatterTask]:
        stmt = select(MatterTask).where(MatterTask.matter_id == matter_id).order_by(MatterTask.created_at.asc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())

    async def update_task_status(self, task_id: str, new_status: str) -> MatterTask:
        if new_status not in self.VALID_STATUSES:
            raise ValidationException(f"Invalid task status '{new_status}'. Allowed: {', '.join(self.VALID_STATUSES)}")

        stmt = select(MatterTask).where(MatterTask.id == task_id)
        task = (await self.db.execute(stmt)).scalars().first()
        if not task:
            raise NotFoundException("MatterTask", task_id)

        task.status = new_status
        await self.db.flush()
        return task
