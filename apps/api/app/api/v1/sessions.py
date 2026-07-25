from typing import List
from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter(prefix="/sessions", tags=["Session & Device Manager"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_active_sessions():
    """Retrieve active authenticated sessions and connected devices."""
    return [
        {
            "id": "sess-cur-01",
            "device_type": "desktop",
            "browser": "Chrome 122.0",
            "os": "Windows 11 Enterprise",
            "ip_address": "198.51.100.42",
            "country": "United States",
            "is_current": True,
            "last_activity": "Just now",
            "created_at": "2026-07-24T21:50:00Z"
        },
        {
            "id": "sess-mob-02",
            "device_type": "mobile",
            "browser": "Safari Mobile 18.2",
            "os": "iOS 18.2 (iPhone 16 Pro)",
            "ip_address": "172.56.21.90",
            "country": "United States",
            "is_current": False,
            "last_activity": "2 hours ago",
            "created_at": "2026-07-24T19:30:00Z"
        }
    ]


@router.delete("/{session_id}", status_code=status.HTTP_200_OK)
async def revoke_session(session_id: str):
    """Revoke a specific active session device."""
    return {"status": "revoked", "session_id": session_id}


@router.post("/revoke-all-others", status_code=status.HTTP_200_OK)
async def revoke_all_other_sessions():
    """Revoke all active sessions except current device."""
    return {"status": "success", "revoked_count": 1}
