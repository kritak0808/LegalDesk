from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.role import Role, Permission
from app.core.permissions import DEFAULT_ROLE_PERMISSIONS


class RBACService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_roles() -> List[dict]:
        roles_list = []
        for name, perms in DEFAULT_ROLE_PERMISSIONS.items():
            roles_list.append({
                "name": name,
                "description": f"Standard enterprise role: {name}",
                "permissions_count": len(perms),
                "permissions": perms,
                "is_system_role": True
            })
        return roles_list

    async def list_all_permissions(self) -> List[dict]:
        modules = [
            "contracts", "cases", "matters", "litigation", "compliance",
            "policies", "governance", "documents", "approvals", "research",
            "administration", "analytics", "ai", "system"
        ]
        actions = [
            "create", "read", "update", "delete", "approve", "review",
            "assign", "share", "export", "archive", "restore", "manage", "configure"
        ]
        perms = []
        for mod in modules:
            for act in actions:
                perms.append({
                    "key": f"{mod}:{act}",
                    "module": mod,
                    "action": act,
                    "description": f"Allows user to {act} {mod}"
                })
        return perms
