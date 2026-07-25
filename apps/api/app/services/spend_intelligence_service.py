from typing import List, Dict, Any


class SpendIntelligenceService:
    @staticmethod
    async def get_law_firm_spend(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "firm_name": "Wachtell, Lipton, Rosen & Katz",
                "practice_area": "M&A & Corporate Governance",
                "total_billed_usd": 6800000.0,
                "billing_model": "Alternative Fee Arrangement (AFA)",
                "billing_accuracy": 99.6,
                "win_rate": 94.0
            },
            {
                "firm_name": "Latham & Watkins LLP",
                "practice_area": "Commercial Litigation & IP",
                "total_billed_usd": 4200000.0,
                "billing_model": "Capped Hourly Rate",
                "billing_accuracy": 98.8,
                "win_rate": 88.5
            }
        ]
