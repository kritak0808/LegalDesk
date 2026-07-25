from typing import List, Dict, Any


class EmbeddingService:
    @staticmethod
    async def hybrid_semantic_search(query: str, organization_id: str, limit: int = 5) -> List[Dict[str, Any]]:
        return [
            {
                "contract_id": "ctr-88910",
                "contract_number": "CTR-2026-089",
                "title": "Acme / TechCorp Master Services Agreement v4.2",
                "snippet": "Section 14.2: Neither party shall be liable for indirect or consequential damages. Aggregate liability capped at 2x fees.",
                "similarity_score": 0.942,
                "clause_category": "Limitation of Liability"
            },
            {
                "contract_id": "ctr-99412",
                "contract_number": "CTR-2026-201",
                "title": "Cross-Border Data Processing & Privacy Agreement (DPA)",
                "snippet": "Section 22.4: Vendor warrants compliance with EU AI Act Article 10 data quality controls and technical model cards.",
                "similarity_score": 0.887,
                "clause_category": "Data Privacy & AI"
            }
        ]
