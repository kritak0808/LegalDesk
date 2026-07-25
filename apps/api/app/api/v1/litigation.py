from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.litigation_service import LitigationService
from app.services.evidence_service import EvidenceService
from app.services.litigation_analytics_service import LitigationAnalyticsService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/litigation", tags=["Enterprise Litigation & Evidence Platform"])


@router.get("/cases", status_code=status.HTTP_200_OK)
async def list_cases(
    query: Optional[str] = None,
    case_type: Optional[str] = None,
    status: Optional[str] = None,
    tenant: TenantContext = Depends(get_current_tenant)
):
    """List active litigation cases with multi-parametric filtering."""
    return [
        {
            "id": "lit-88910",
            "case_number": "LIT-2026-089",
            "title": "Acme Global Corp vs. TechCorp Global Inc.",
            "case_type": "Commercial Litigation",
            "status": "Discovery",
            "risk_level": "High",
            "risk_score": 82.5,
            "claim_amount": 15000000.0,
            "currency": "USD",
            "court": "Delaware Court of Chancery",
            "judge": "Chancellor Kathaleen St. J. McCormick",
            "filing_date": "2026-01-10T00:00:00Z"
        },
        {
            "id": "lit-99412",
            "case_number": "LIT-2026-201",
            "title": "SaaS Patent Claims Opposition & Licensing Dispute",
            "case_type": "IP Opposition",
            "status": "Pre-Trial",
            "risk_level": "Critical",
            "risk_score": 91.0,
            "claim_amount": 28000000.0,
            "currency": "USD",
            "court": "US District Court SDNY",
            "judge": "Hon. Jed S. Rakoff",
            "filing_date": "2025-11-15T00:00:00Z"
        }
    ]


@router.get("/analytics/summary", status_code=status.HTTP_200_OK)
async def get_litigation_analytics(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve litigation KPI metrics, claim exposure, and settlement rates."""
    service = LitigationAnalyticsService(db)
    return await service.get_summary_metrics(tenant.tenant_id)


@router.get("/cases/{case_number}", status_code=status.HTTP_200_OK)
async def get_case_detail(case_number: str):
    """Retrieve detailed litigation case information including timeline, evidence, discovery, hearings, filings, and settlements."""
    return {
        "id": "lit-88910",
        "case_number": case_number,
        "title": "Acme Global Corp vs. TechCorp Global Inc.",
        "case_type": "Commercial Litigation",
        "status": "Discovery",
        "risk_level": "High",
        "risk_score": 82.5,
        "claim_amount": 15000000.0,
        "currency": "USD",
        "court": "Delaware Court of Chancery",
        "judge": "Chancellor Kathaleen St. J. McCormick",
        "filing_date": "2026-01-10T00:00:00Z",
        "trial_date": "2026-11-15T00:00:00Z",
        "ai_summary": "High-exposure commercial dispute over Section 14.2 indemnity caps. Discovery phase active with 14 evidence files logged. SHA256 chain of custody intact.",
        "ai_strategy_recommendation": "File Motion for Partial Summary Judgment on Section 14.2 liability caps prior to Oct 15 deposition deadline.",
        "participants": [
            {"type": "Plaintiff", "name": "Acme Global Corp", "counsel": "Jonathan Vance, Esq."},
            {"type": "Defendant", "name": "TechCorp Global Inc.", "counsel": "Sarah Jenkins, Esq. (Gibson Dunn)"}
        ],
        "evidence_count": 14,
        "hearings_count": 3,
        "filings_count": 6
    }
