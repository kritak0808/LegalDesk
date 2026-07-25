from typing import List, Dict, Any


class RuleEngine:
    @staticmethod
    async def list_business_rules(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "rule_code": "RUL-2026-001",
                "title": "High Contract Value Executive Routing Rule",
                "module": "Contracts",
                "condition": "Contract Total Value >= $1,000,000",
                "action": "Require General Counsel & CFO Approval",
                "is_active": True
            },
            {
                "rule_code": "RUL-2026-002",
                "title": "Uncapped Consequential Indemnity Risk Routing",
                "module": "Risk",
                "condition": "AI Risk Score >= 80 OR Consequential Indemnity Uncapped",
                "action": "Auto-Trigger Litigation Risk Review & Board Brief",
                "is_active": True
            }
        ]
