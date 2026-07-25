from typing import Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.audit_log import AuditLog
from app.core.logging import logger


class AuditService:
    @staticmethod
    async def log_event(
        db: AsyncSession,
        action: str,
        resource_type: str,
        user_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        resource_id: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ) -> AuditLog:
        audit_entry = AuditLog(
            action=action,
            resource_type=resource_type,
            user_id=user_id,
            organization_id=organization_id,
            resource_id=resource_id,
            ip_address=ip_address,
            user_agent=user_agent,
            details=details or {}
        )
        db.add(audit_entry)
        await db.flush()
        
        logger.info(
            "audit_event_logged",
            action=action,
            resource_type=resource_type,
            user_id=user_id,
            organization_id=organization_id
        )
        return audit_entry
