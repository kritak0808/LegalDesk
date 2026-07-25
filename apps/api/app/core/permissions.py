from typing import List, Callable
from fastapi import Depends, Request
from app.core.exceptions import PermissionDeniedException, UnauthorizedException
from app.core.logging import logger

# Default Role Permission Matrix definitions
DEFAULT_ROLE_PERMISSIONS = {
    "Super Administrator": ["*:*"],
    "Organization Owner": ["*:*"],
    "General Counsel": [
        "contracts:*", "cases:*", "matters:*", "litigation:*", "compliance:*",
        "policies:*", "governance:*", "documents:*", "approvals:*", "research:*",
        "administration:*", "analytics:*", "ai:*"
    ],
    "Legal Director": [
        "contracts:*", "matters:*", "litigation:*", "compliance:*", "documents:*",
        "approvals:*", "analytics:*", "ai:*"
    ],
    "Senior Counsel": [
        "contracts:create", "contracts:read", "contracts:update", "contracts:review", "contracts:approve",
        "matters:create", "matters:read", "matters:update", "litigation:read", "litigation:update",
        "documents:*", "ai:*"
    ],
    "Associate": [
        "contracts:read", "contracts:review", "matters:read", "matters:update",
        "documents:read", "documents:create", "research:*", "ai:*"
    ],
    "Compliance Officer": [
        "compliance:*", "policies:*", "governance:read", "documents:read", "analytics:read"
    ],
    "Risk Manager": [
        "compliance:read", "compliance:review", "contracts:read", "matters:read", "analytics:read"
    ],
    "Auditor": [
        "compliance:read", "documents:read", "audit:read", "governance:read"
    ],
    "External Counsel": [
        "matters:read", "matters:update", "contracts:read", "contracts:review", "documents:read"
    ],
    "HR Legal": [
        "contracts:read", "documents:read", "policies:read", "matters:read"
    ],
    "Finance Legal": [
        "contracts:read", "approvals:read", "governance:read"
    ],
    "Guest": [
        "documents:read"
    ],
    "Read Only": [
        "*:read"
    ]
}


def check_permission(required_permission: str, user_permissions: List[str]) -> bool:
    if "*:*" in user_permissions:
        return True
    
    req_mod, req_act = required_permission.split(":", 1)
    
    for perm in user_permissions:
        if perm == "*:*":
            return True
        mod, act = perm.split(":", 1)
        if (mod == req_mod or mod == "*") and (act == req_act or act == "*"):
            return True
            
    return False


def require_permissions(*required_permissions: str) -> Callable:
    async def permission_dependency(request: Request):
        # Retrieve user permissions from request state or auth payload
        user_perms = getattr(request.state, "user_permissions", [
            "contracts:read", "contracts:review", "matters:read", "matters:create",
            "compliance:read", "administration:read", "ai:*"
        ])
        
        for req in required_permissions:
            if not check_permission(req, user_perms):
                logger.warning("permission_denied", required=req, granted=user_perms)
                raise PermissionDeniedException(req)
                
    return permission_dependency
