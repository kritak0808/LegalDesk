from typing import List, Dict, Any


class BoardReportingService:
    @staticmethod
    async def get_board_packs(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "report_number": "BRD-REP-2026-Q1",
                "title": "Q1 2026 Enterprise Legal, Regulatory Risk & Board Briefing",
                "period": "Q1 2026",
                "status": "Finalized",
                "pdf_export_url": "/api/v1/executive/board-reports/BRD-REP-2026-Q1/export.pdf",
                "sections": [
                    "1. Executive Summary & Legal Portfolio Health",
                    "2. EU AI Act Article 10 Compliance & Governance Audit",
                    "3. Delaware Chancery Litigation Exposure ($15M Case / $84.5M Total)",
                    "4. Outside Counsel Spend vs Budget ($14.2M Allocated)"
                ]
            }
        ]
