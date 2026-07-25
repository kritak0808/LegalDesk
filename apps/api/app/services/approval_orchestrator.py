from typing import List, Dict, Any


class ApprovalOrchestrator:
    @staticmethod
    async def get_pending_approvals(user_id: str, organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "approval_id": "appr-001",
                "entity_number": "CTR-2026-089",
                "entity_title": "Global Enterprise Master Services Agreement (MSA)",
                "requester": "Sarah Jenkins, VP Sales",
                "step_name": "General Counsel Approval",
                "contract_value": "$2,500,000",
                "ai_risk_score": "22.4 (Low Risk)",
                "hours_remaining": 33,
                "status": "Pending Signoff"
            }
        ]
