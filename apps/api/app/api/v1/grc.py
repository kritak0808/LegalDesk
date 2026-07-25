from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.compliance_service import ComplianceService
from app.services.policy_service import PolicyService
from app.services.risk_service import RiskService
from app.services.ai_governance_service import AIGovernanceService
from app.services.grc_analytics_service import GRCAnalyticsService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/grc", tags=["Enterprise Compliance, Governance & Risk (GRC)"])


@router.get("/frameworks", status_code=status.HTTP_200_OK)
async def list_frameworks(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve regulatory frameworks library (GDPR, EU AI Act, SOC 2, ISO 27001, HIPAA, CCPA)."""
    service = ComplianceService(db)
    return await service.list_frameworks(tenant.tenant_id)


@router.get("/policies", status_code=status.HTTP_200_OK)
async def list_policies(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve enterprise policy registry and acknowledgment progress."""
    service = PolicyService(db)
    return await service.list_policies(tenant.tenant_id)


@router.get("/risks", status_code=status.HTTP_200_OK)
async def get_risk_register(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve Enterprise Risk Register and Likelihood x Impact scores."""
    service = RiskService(db)
    return await service.get_risk_register(tenant.tenant_id)


@router.get("/ai-governance", status_code=status.HTTP_200_OK)
async def get_ai_model_registry(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve AI Model Registry and EU AI Act Article 10 classification cards."""
    return await AIGovernanceService.get_model_registry(tenant.tenant_id)


@router.get("/analytics/summary", status_code=status.HTTP_200_OK)
async def get_grc_analytics(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve executive GRC scorecard metrics, coverage, and open incidents."""
    service = GRCAnalyticsService(db)
    return await service.get_summary_metrics(tenant.tenant_id)
