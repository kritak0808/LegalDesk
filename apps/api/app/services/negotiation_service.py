from typing import Dict, Any


class NegotiationService:
    @staticmethod
    async def generate_clause_rewrites(clause_text: str, category: str) -> Dict[str, Any]:
        return {
            "original_clause": clause_text,
            "category": category,
            "business_friendly_option": "Neither party shall be liable for indirect or consequential damages. Liability is capped at 1x total fees paid under this Agreement.",
            "legal_friendly_option": "Except for gross negligence or willful misconduct, neither party's aggregate liability under this Agreement shall exceed 2x fees paid in the trailing 12 months.",
            "fallback_option": "Aggregate liability shall not exceed total fees paid by Customer during the 12-month period immediately preceding the claim.",
            "explanation": "Legal-friendly option balances liability exposure while preserving standard Delaware Chancery precedents."
        }
