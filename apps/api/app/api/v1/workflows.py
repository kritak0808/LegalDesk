from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.workflow_service import WorkflowService
from app.services.execution_engine import ExecutionEngine
from app.services.rule_engine import RuleEngine
from app.services.approval_orchestrator import ApprovalOrchestrator
from app.services.workflow_analytics_service import WorkflowAnalyticsService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/workflows", tags=["Enterprise Workflow Automation & Decision Engine"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_workflows(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve published workflow definitions and node-graph templates."""
    service = WorkflowService(db)
    return await service.list_workflows(tenant.tenant_id)


@router.get("/executions", status_code=status.HTTP_200_OK)
async def get_active_executions(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve real-time running process executions, step states, and SLA timers."""
    return await ExecutionEngine.get_active_executions(tenant.tenant_id)


@router.get("/rules", status_code=status.HTTP_200_OK)
async def list_business_rules(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve configurable business rules, threshold conditions, and risk routing."""
    return await RuleEngine.list_business_rules(tenant.tenant_id)


@router.get("/approvals/pending", status_code=status.HTTP_200_OK)
async def get_pending_approvals(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve pending approval queues with SLA countdowns and AI risk scores."""
    return await ApprovalOrchestrator.get_pending_approvals("usr-001", tenant.tenant_id)


@router.get("/analytics/summary", status_code=status.HTTP_200_OK)
async def get_workflow_analytics(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve workflow analytics, turnaround savings ($480k), and SLA compliance rates (97.8%)."""
    service = WorkflowAnalyticsService(db)
    return await service.get_summary_metrics(tenant.tenant_id)
