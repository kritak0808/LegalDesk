from typing import List
from fastapi import APIRouter, Depends, status
from app.services.rbac_service import RBACService
from app.core.permissions import require_permissions

router = APIRouter(prefix="/roles", tags=["RBAC & Permissions Engine"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_roles():
    """Retrieve enterprise system roles and permission assignments."""
    return await RBACService.list_roles()


@router.get("/permissions", status_code=status.HTTP_200_OK)
async def list_all_permissions():
    """Retrieve full catalog of module:action permissions for role matrix configuration."""
    return await RBACService.list_all_permissions()
