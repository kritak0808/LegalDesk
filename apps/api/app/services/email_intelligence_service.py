from typing import List, Dict, Any


class EmailIntelligenceService:
    @staticmethod
    async def get_matter_emails(matter_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "email_id": "eml-001",
                "subject": "RE: Delaware Court of Chancery Motion to Dismiss Hearing Confirmation",
                "sender": "latham_partner@lathamwatkins.com",
                "received_at": "2026-07-24 14:22:00",
                "ai_classification": "Litigation Correspondence",
                "linked_matter": matter_id,
                "attachments_count": 2
            }
        ]
