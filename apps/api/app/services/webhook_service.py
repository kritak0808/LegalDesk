from typing import List, Dict, Any


class WebhookService:
    @staticmethod
    async def list_subscriptions(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "id": "wh-001",
                "target_url": "https://api.enterprise.com/hooks/legaldesk-events",
                "subscribed_events": ["matter.created", "contract.signed", "risk.updated", "workflow.completed"],
                "status": "Active (100% Delivery Success Rate)",
                "signing_secret": "whsec_live_9847291847"
            }
        ]
