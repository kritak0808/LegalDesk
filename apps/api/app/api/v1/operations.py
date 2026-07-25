from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.operations_service import OperationsService
from app.services.tracing_service import TracingService
from app.services.security_operations_service import SecurityOperationsService
from app.services.job_monitoring_service import JobMonitoringService
from app.services.backup_recovery_service import BackupRecoveryService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/operations", tags=["Enterprise Platform Operations & Reliability"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def get_platform_health(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve platform availability (99.99%), SLA status, and component health matrix."""
    service = OperationsService(db)
    return await service.get_platform_health_matrix(tenant.tenant_id)


@router.get("/traces", status_code=status.HTTP_200_OK)
async def get_recent_traces():
    """Retrieve distributed request traces, correlation IDs, and P99 latency spans."""
    return await TracingService.get_recent_traces()


@router.get("/security", status_code=status.HTTP_200_OK)
async def get_security_events(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve SOC threat detection logs, authentication monitoring, and permission audits."""
    return await SecurityOperationsService.get_security_events(tenant.tenant_id)


@router.get("/jobs", status_code=status.HTTP_200_OK)
async def get_background_queues():
    """Retrieve Celery worker queue depth, execution latency, and retry history."""
    return await JobMonitoringService.get_background_queues()


@router.get("/backups", status_code=status.HTTP_200_OK)
async def list_backups(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve point-in-time database backups, AES-256 encryption status, and recovery drills."""
    return await BackupRecoveryService.list_backups(tenant.tenant_id)
