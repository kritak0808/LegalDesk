from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.executive_intelligence_service import ExecutiveIntelligenceService
from app.services.spend_intelligence_service import SpendIntelligenceService
from app.services.predictive_analytics_service import PredictiveAnalyticsService
from app.services.board_reporting_service import BoardReportingService
from app.services.executive_copilot_service import ExecutiveCopilotService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/executive", tags=["Enterprise Executive Intelligence & Decision Engine"])


@router.get("/command-center", status_code=status.HTTP_200_OK)
async def get_command_center(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve Executive Command Center metrics: Enterprise Health Score (96.4%), Risk Index, Litigation Exposure."""
    service = ExecutiveIntelligenceService(db)
    return await service.get_command_center_metrics(tenant.tenant_id)


@router.get("/spend", status_code=status.HTTP_200_OK)
async def get_legal_spend(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve Outside Counsel spend ($14.2M), law firm win rates, and billing accuracy ratings."""
    return await SpendIntelligenceService.get_law_firm_spend(tenant.tenant_id)


@router.get("/predictions", status_code=status.HTTP_200_OK)
async def get_predictive_analytics(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve AI predictive models: settlement probabilities (78.4%), litigation outcomes, and contract delay risks."""
    return await PredictiveAnalyticsService.get_forecasts(tenant.tenant_id)


@router.get("/board-reports", status_code=status.HTTP_200_OK)
async def get_board_reports(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve finalized Board Packs, quarterly risk reports, and PDF export URLs."""
    return await BoardReportingService.get_board_packs(tenant.tenant_id)


@router.post("/copilot/query", status_code=status.HTTP_200_OK)
async def query_executive_copilot(
    query: str = Body(..., embed=True),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """AI Executive Copilot: Natural language Q&A ('What changed this week?', 'What is our highest legal risk?')."""
    return await ExecutiveCopilotService.query_executive_copilot(query, tenant.tenant_id)
