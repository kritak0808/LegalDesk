from typing import List, Dict, Any


class SignatureService:
    @staticmethod
    async def get_envelopes(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "envelope_number": "ENV-2026-089",
                "provider": "DocuSign Enterprise",
                "subject": "Global Enterprise Master Services Agreement (MSA)",
                "status": "Completed & Fully Executed",
                "recipients": [
                    {"name": "Jonathan Vance", "role": "General Counsel", "status": "Signed"},
                    {"name": "Sarah Jenkins", "role": "VP Sales", "status": "Signed"}
                ],
                "completed_at": "2026-07-24 16:45:00"
            }
        ]
