from typing import List, Optional
from fastapi import APIRouter, status, Query

router = APIRouter(prefix="/audit-logs", tags=["Audit Logging System"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_audit_logs(
    limit: int = Query(20, ge=1, le=100),
    action: Optional[str] = None
):
    """Retrieve system audit logs filterable by action type and user."""
    logs = [
        {
            "id": "aud-01",
            "action": "AUTH.LOGIN",
            "resource_type": "Session",
            "user_name": "Jonathan Vance, Esq.",
            "ip_address": "198.51.100.42",
            "user_agent": "Chrome 122 (Windows 11)",
            "timestamp": "2026-07-24T21:50:12Z",
            "status": "SUCCESS"
        },
        {
            "id": "aud-02",
            "action": "ROLE.CHANGED",
            "resource_type": "UserRole",
            "user_name": "Jonathan Vance, Esq.",
            "ip_address": "198.51.100.42",
            "details": {"target_user": "Sarah Jenkins", "new_role": "External Counsel"},
            "timestamp": "2026-07-24T20:14:02Z",
            "status": "SUCCESS"
        },
        {
            "id": "aud-03",
            "action": "INVITATION.SENT",
            "resource_type": "Invitation",
            "user_name": "Jonathan Vance, Esq.",
            "ip_address": "198.51.100.42",
            "details": {"invited_email": "audit.compliance@big4audit.com", "user_type": "auditor"},
            "timestamp": "2026-07-24T18:45:22Z",
            "status": "SUCCESS"
        },
        {
            "id": "aud-04",
            "action": "SESSION.REVOKED",
            "resource_type": "Session",
            "user_name": "Jonathan Vance, Esq.",
            "ip_address": "198.51.100.42",
            "details": {"revoked_session_id": "sess-old-881"},
            "timestamp": "2026-07-24T16:10:00Z",
            "status": "SUCCESS"
        }
    ]
    if action:
        logs = [l for l in logs if l["action"] == action]
    return logs[:limit]
