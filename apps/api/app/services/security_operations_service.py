from typing import List, Dict, Any


class SecurityOperationsService:
    @staticmethod
    async def get_security_events(organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "event_id": "sec-001",
                "event_type": "Suspicious Login Location Throttled",
                "severity": "Medium",
                "source_ip": "198.51.100.42",
                "timestamp": "2026-07-24 15:10:00",
                "description": "Multi-factor authentication challenge triggered due to novel IP address.",
                "action_taken": "MFA Enforced & Session Logged"
            }
        ]
