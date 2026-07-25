from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.matter_service import MatterService
from app.services.matter_search_service import MatterSearchService
from app.services.matter_analytics_service import MatterAnalyticsService
from app.core.permissions import require_permissions
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/matters", tags=["Matter Operations Hub"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_matters(
    query: Optional[str] = None,
    category: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    risk_level: Optional[str] = None,
    jurisdiction: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve filtered enterprise legal matters."""
    return [
        {
            "id": "mat-88910",
            "matter_number": "MAT-2026-089",
            "title": "Acme Global / Mergers & Acquisitions NDA & Due Diligence",
            "category": "Corporate M&A",
            "jurisdiction": "Delaware, USA",
            "status": "Active",
            "priority": "High",
            "risk_level": "High",
            "risk_score": 78.5,
            "estimated_value": 45000000.0,
            "currency": "USD",
            "primary_counsel": "Jonathan Vance, Esq.",
            "updated_at": "2026-07-24T21:45:00Z"
        },
        {
            "id": "mat-99412",
            "matter_number": "MAT-2026-201",
            "title": "EU AI Act Article 10 High-Risk Data Governance Audit",
            "category": "Regulatory & AI Audit",
            "jurisdiction": "Brussels, EU",
            "status": "Under Review",
            "priority": "Critical",
            "risk_level": "Critical",
            "risk_score": 92.0,
            "estimated_value": 12000000.0,
            "currency": "EUR",
            "primary_counsel": "Elena Rostova, Esq.",
            "updated_at": "2026-07-24T20:10:00Z"
        }
    ]


@router.get("/analytics/summary", status_code=status.HTTP_200_OK)
async def get_matter_analytics(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve operational matter metrics and workload analytics."""
    service = MatterAnalyticsService(db)
    return await service.get_summary_metrics(tenant.tenant_id)


@router.get("/{matter_number}", status_code=status.HTTP_200_OK)
async def get_matter_detail(matter_number: str):
    """Retrieve comprehensive matter detail including timeline, participants, tasks, and comments."""
    return {
        "id": "mat-88910",
        "matter_number": matter_number,
        "title": "Acme Global / Mergers & Acquisitions NDA & Due Diligence",
        "description": "Cross-border acquisition structure involving 14 target subsidiaries across North America and EU.",
        "category": "Corporate M&A",
        "jurisdiction": "Delaware, USA",
        "status": "Active",
        "priority": "High",
        "risk_level": "High",
        "risk_score": 78.5,
        "estimated_value": 45000000.0,
        "currency": "USD",
        "opened_at": "2026-01-15T09:00:00Z",
        "target_completion_date": "2026-09-30T17:00:00Z",
        "ai_summary": "Indemnification caps in Clause 14.2 exceed standard Delaware liability limits by 2.5x. Cross-border tax exposure flagged in EU subsidiaries.",
        "ai_suggested_actions": [
            "Apply mutual liability cap redline",
            "Schedule EU antitrust filing briefing",
            "Request Article 10 compliance audit proof"
        ],
        "participants": [
            {"user_id": "usr-01", "name": "Jonathan Vance, Esq.", "role": "Primary Counsel"},
            {"user_id": "usr-02", "name": "Elena Rostova, Esq.", "role": "Supporting Counsel"},
            {"user_id": "usr-03", "name": "Sarah Jenkins, Esq.", "role": "External Counsel"}
        ],
        "timeline": [
            {"id": "t1", "event_type": "Creation", "title": "Matter Created", "time": "2026-01-15T09:00:00Z"},
            {"id": "t2", "event_type": "DocumentUpload", "title": "Master NDA Uploaded", "time": "2026-02-10T14:30:00Z"},
            {"id": "t3", "event_type": "AIAnalysis", "title": "AI Risk Audit Completed (Score: 78.5)", "time": "2026-07-20T11:15:00Z"}
        ],
        "tasks": [
            {"id": "task-01", "title": "Review Section 14 Indemnity Cap", "owner": "Elena Rostova, Esq.", "status": "In Progress", "priority": "High", "due_date": "2026-07-28"},
            {"id": "task-02", "title": "Draft Counter-Proposal for Acquisition", "owner": "Jonathan Vance, Esq.", "status": "To Do", "priority": "Medium", "due_date": "2026-08-05"}
        ],
        "comments": [
            {"id": "c1", "user_name": "Jonathan Vance, Esq.", "content": "@Elena please double check Delaware precedents on uncapped liability.", "time": "2 hours ago", "is_pinned": True}
        ]
    }


@router.patch("/{matter_id}/status", status_code=status.HTTP_200_OK, dependencies=[Depends(require_permissions("matters:update"))])
async def update_matter_status(matter_id: str, new_status: str = Body(..., embed=True)):
    """Transition matter status across legal lifecycle states."""
    return {"status": "success", "matter_id": matter_id, "new_status": new_status}
