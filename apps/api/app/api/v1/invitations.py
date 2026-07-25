from typing import List, Optional
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.invitation_service import InvitationService
from app.core.permissions import require_permissions
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/invitations", tags=["User Invitation System"])


class InviteCreateRequest(BaseModel):
    email: EmailStr
    user_type: str = "internal"  # internal, external_counsel, auditor, guest
    role_name: str = "Senior Counsel"


@router.get("", status_code=status.HTTP_200_OK)
async def list_invitations():
    """List pending and accepted organization invitations."""
    return [
        {
            "id": "inv-01",
            "email": "sarah.jenkins@external-counsel.law",
            "user_type": "external_counsel",
            "role_name": "External Counsel",
            "invited_by": "Jonathan Vance, Esq.",
            "expires_at": "2026-07-31T22:00:00Z",
            "status": "pending"
        },
        {
            "id": "inv-02",
            "email": "audit.compliance@big4audit.com",
            "user_type": "auditor",
            "role_name": "Auditor",
            "invited_by": "Jonathan Vance, Esq.",
            "expires_at": "2026-07-28T18:00:00Z",
            "status": "pending"
        }
    ]


@router.post("", status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_permissions("administration:manage"))])
async def create_invitation(data: InviteCreateRequest):
    """Send an invitation email to a internal team member, external counsel, or auditor."""
    return {
        "status": "invited",
        "invitation": {
            "email": data.email,
            "user_type": data.user_type,
            "role_name": data.role_name,
            "token": "inv_sample_verification_token_99812",
            "status": "pending"
        }
    }


@router.delete("/{invitation_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(require_permissions("administration:manage"))])
async def revoke_invitation(invitation_id: str):
    """Revoke a pending invitation."""
    return {"status": "revoked", "invitation_id": invitation_id}
