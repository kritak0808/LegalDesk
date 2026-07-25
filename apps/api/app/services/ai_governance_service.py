from typing import List, Dict, Any


class AIGovernanceService:
    @staticmethod
    async def get_model_registry(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "id": "aim-001",
                "model_name": "LegalDesk RAG Contract Analyzer v5.0",
                "risk_classification": "High Risk (EU AI Act Article 10)",
                "bias_audit_status": "Passed (99.2% Fairness)",
                "explainability_score": 96.5,
                "human_in_loop_required": True,
                "model_owner": "Jonathan Vance, General Counsel",
                "status": "Active & Compliant"
            },
            {
                "id": "aim-002",
                "model_name": "LegalDesk Clause Summarization LLM",
                "risk_classification": "Limited Risk",
                "bias_audit_status": "Passed",
                "explainability_score": 98.0,
                "human_in_loop_required": False,
                "model_owner": "AI Compliance Team",
                "status": "Active"
            }
        ]
