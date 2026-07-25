from typing import Dict, Any, List


class KnowledgeGraphService:
    @staticmethod
    async def get_legal_knowledge_graph(organization_id: str) -> Dict[str, Any]:
        return {
            "nodes": [
                {"id": "n1", "label": "Acme Global Corp", "type": "Organization"},
                {"id": "n2", "label": "TechCorp Global Inc.", "type": "Organization"},
                {"id": "n3", "label": "CTR-2026-089 (TechCorp MSA)", "type": "Contract"},
                {"id": "n4", "label": "MAT-2026-089 (M&A Due Diligence)", "type": "Matter"},
                {"id": "n5", "label": "Clause 14.2 (Liability Cap)", "type": "Clause"},
                {"id": "n6", "label": "EU AI Act Article 10", "type": "Regulation"},
                {"id": "n7", "label": "Jonathan Vance, General Counsel", "type": "Person"}
            ],
            "edges": [
                {"source": "n1", "target": "n3", "label": "PARTY_TO"},
                {"source": "n2", "target": "n3", "label": "PARTY_TO"},
                {"source": "n3", "target": "n4", "label": "LINKED_TO"},
                {"source": "n3", "target": "n5", "label": "CONTAINS"},
                {"source": "n3", "target": "n6", "label": "REGULATED_BY"},
                {"source": "n7", "target": "n4", "label": "LEAD_COUNSEL"}
            ]
        }
