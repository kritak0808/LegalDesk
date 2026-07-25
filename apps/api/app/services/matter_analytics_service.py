from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession


class MatterAnalyticsService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_summary_metrics(self, organization_id: str) -> Dict[str, Any]:
        return {
            "total_matters": 48,
            "open_matters": 34,
            "closed_matters": 14,
            "high_risk_matters": 7,
            "pending_approvals": 5,
            "avg_resolution_days": 18.4,
            "status_distribution": {
                "Active": 18,
                "Under Review": 8,
                "Pending Approval": 5,
                "Escalated": 3,
                "Closed": 14
            },
            "category_distribution": {
                "Corporate M&A": 12,
                "Contract Review": 16,
                "Regulatory & AI Audit": 10,
                "Litigation": 6,
                "Employment": 4
            },
            "risk_distribution": {
                "Low": 20,
                "Medium": 21,
                "High": 5,
                "Critical": 2
            }
        }
