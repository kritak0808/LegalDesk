from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.research_service import ResearchService
from app.services.citation_service import CitationService
from app.services.memorandum_service import MemorandumService
from app.services.ai_research_assistant_service import AIResearchAssistantService
from app.services.research_analytics_service import ResearchAnalyticsService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/research", tags=["Enterprise Legal Research & Precedent Intelligence"])


@router.get("/search", status_code=status.HTTP_200_OK)
async def search_legal_sources(
    query: str = Query("Delaware consequential damage liability caps"),
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Execute hybrid semantic & citation search across case law judgments, statutes, and internal memos."""
    service = ResearchService(db)
    return await service.search_legal_sources(query, tenant.tenant_id)


@router.get("/citations/validate", status_code=status.HTTP_200_OK)
async def validate_citation(citation: str = Query("650 A.2d 1270 (Del. 1994)")):
    """Validate legal citations and calculate authority rank scores (0-100)."""
    return await CitationService.validate_citation(citation)


@router.get("/memorandums", status_code=status.HTTP_200_OK)
async def list_memorandums(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve enterprise legal memorandums and approval workflows."""
    service = MemorandumService(db)
    return await service.list_memorandums(tenant.tenant_id)


@router.post("/ai/assist", status_code=status.HTTP_200_OK)
async def ai_research_assist(
    query: str = Body(..., embed=True),
    matter_id: str = Body("MAT-2026-089", embed=True)
):
    """AI Legal Research Assistant: Auto-draft research memos, spot issues, and map supporting vs opposing authorities."""
    return await AIResearchAssistantService.generate_research_memo(query, matter_id)


@router.get("/analytics/summary", status_code=status.HTTP_200_OK)
async def get_research_analytics(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve research activity, citation validation counts, and authority rankings."""
    service = ResearchAnalyticsService(db)
    return await service.get_summary_metrics(tenant.tenant_id)
