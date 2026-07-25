from typing import Dict, Any


class ParserService:
    @staticmethod
    async def parse_legal_contract(contract_id: str, text: str) -> Dict[str, Any]:
        return {
            "contract_id": contract_id,
            "title": "Master Services Agreement",
            "parties": ["Acme Global Corporation Inc.", "TechCorp Global Inc."],
            "governing_law": "Delaware State Law",
            "jurisdiction": "Delaware, USA",
            "effective_date": "2026-02-01",
            "expiration_date": "2028-02-01",
            "total_value": 4500000.0,
            "currency": "USD",
            "notice_period_days": 60,
            "key_clauses_extracted": {
                "indemnity": "Section 14.2 — Uncapped mutual indemnification",
                "liability_cap": "Section 14.3 — Capped at 2x 12-month trailing fees",
                "data_privacy": "Section 22.4 — EU AI Act Article 10 & GDPR compliance",
                "termination": "Section 18.1 — 60-day written notice for convenience"
            }
        }
