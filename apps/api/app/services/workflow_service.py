from typing import List, Dict, Any
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.workflow import Workflow


class WorkflowService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_workflows(self, organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "id": "wfk-001",
                "workflow_number": "WFK-2026-001",
                "title": "High-Value MSA Contract Approval & AI Risk Audit Workflow",
                "category": "Contracts",
                "status": "Published",
                "current_version": "v1.2",
                "trigger_type": "Contract Created",
                "active_executions_count": 14,
                "avg_turnaround_hours": 18.5
            },
            {
                "id": "wfk-002",
                "workflow_number": "WFK-2026-002",
                "title": "Litigation Filing & Evidence Chain-of-Custody Escalation",
                "category": "Litigation",
                "status": "Published",
                "current_version": "v2.0",
                "trigger_type": "Case Filed",
                "active_executions_count": 6,
                "avg_turnaround_hours": 12.0
            }
        ]
