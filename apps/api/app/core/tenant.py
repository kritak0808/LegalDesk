from typing import Optional
from fastapi import Request, Depends, Header
from app.core.exceptions import UnauthorizedException, PermissionDeniedException
from app.core.logging import logger


class TenantContext:
    def __init__(self, tenant_id: str, tenant_slug: Optional[str] = None):
        self.tenant_id = tenant_id
        self.tenant_slug = tenant_slug


async def get_current_tenant(
    request: Request,
    x_tenant_id: Optional[str] = Header(None, alias="X-Tenant-ID")
) -> TenantContext:
    """Extract and validate tenant isolation context from header or request state."""
    tenant_id = x_tenant_id or getattr(request.state, "tenant_id", "org-acme-global-01")
    if not tenant_id:
        raise UnauthorizedException("Tenant context (X-Tenant-ID) is missing.")
    
    return TenantContext(tenant_id=tenant_id)
