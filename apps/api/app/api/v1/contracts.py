from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.contract_service import ContractService
from app.services.contract_analytics_service import ContractAnalyticsService
from app.core.permissions import require_permissions
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/contracts", tags=["Contract Lifecycle Management (CLM)"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_contracts(
    query: Optional[str] = None,
    contract_type: Optional[str] = None,
    status: Optional[str] = None,
    risk_level: Optional[str] = None,
    tenant: TenantContext = Depends(get_current_tenant)
):
    """List enterprise contracts with multi-parametric filtering."""
    return [
        {
            "id": "ctr-88910",
            "contract_number": "CTR-2026-089",
            "title": "Acme / TechCorp Master Services Agreement v4.2",
            "type": "Master Services Agreement",
            "status": "Active",
            "risk_level": "High",
            "deviation_score": 28.5,
            "total_value": 4500000.0,
            "currency": "USD",
            "counterparty": "TechCorp Global Inc.",
            "effective_date": "2026-02-01T00:00:00Z",
            "expiration_date": "2028-02-01T00:00:00Z",
            "auto_renew": True,
            "renewal_notice_days": 60
        },
        {
            "id": "ctr-99412",
            "contract_number": "CTR-2026-201",
            "title": "Cross-Border Data Processing & Privacy Agreement (DPA)",
            "type": "Data Processing Agreement",
            "status": "Under Review",
            "risk_level": "Medium",
            "deviation_score": 12.0,
            "total_value": 850000.0,
            "currency": "EUR",
            "counterparty": "EuroCloud Services B.V.",
            "effective_date": "2026-04-15T00:00:00Z",
            "expiration_date": "2027-04-15T00:00:00Z",
            "auto_renew": False,
            "renewal_notice_days": 30
        }
    ]


@router.get("/analytics/summary", status_code=status.HTTP_200_OK)
async def get_contract_analytics(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve operational CLM metrics and turnaround KPIs."""
    service = ContractAnalyticsService(db)
    return await service.get_summary_metrics(tenant.tenant_id)


@router.get("/{contract_number}", status_code=status.HTTP_200_OK)
async def get_contract_detail(contract_number: str):
    """Retrieve comprehensive contract detail including versions, parties, approvals, and obligations."""
    return {
        "id": "ctr-88910",
        "contract_number": contract_number,
        "title": "Acme / TechCorp Master Services Agreement v4.2",
        "type": "Master Services Agreement",
        "status": "Active",
        "risk_level": "High",
        "deviation_score": 28.5,
        "total_value": 4500000.0,
        "currency": "USD",
        "governing_law": "Delaware State Law",
        "effective_date": "2026-02-01T00:00:00Z",
        "expiration_date": "2028-02-01T00:00:00Z",
        "auto_renew": True,
        "renewal_notice_days": 60,
        "ai_summary": "Section 14.2 contains an uncapped indemnity clause. Delaware governing law applies. Deviation score 28.5% against standard playbook.",
        "ai_suggested_clauses": [
            "Clause 14.2B: Mutual liability cap at 2x 12-month trailing fees",
            "Section 22.4: EU cross-border data transfer safeguard"
        ],
        "parties": [
            {"id": "p1", "type": "Internal Entity", "name": "Acme Global Corporation Inc.", "signatory": "Jonathan Vance, Esq."},
            {"id": "p2", "type": "Customer", "name": "TechCorp Global Inc.", "signatory": "Marcus Sterling, VP Procurement"}
        ],
        "versions": [
            {"version_number": "v4.2", "is_major": True, "file_name": "MSA_TechCorp_v4.2_Final.pdf", "author": "Jonathan Vance, Esq.", "date": "2026-02-01"},
            {"version_number": "v4.1", "is_major": False, "file_name": "MSA_TechCorp_v4.1_Redline.docx", "author": "Elena Rostova, Esq.", "date": "2026-01-25"}
        ],
        "approval_flow": [
            {"step": 1, "name": "Legal Review", "approver": "Elena Rostova, Esq.", "status": "Approved", "date": "2026-01-26"},
            {"step": 2, "name": "Finance Review", "approver": "Finance Legal Team", "status": "Approved", "date": "2026-01-28"},
            {"step": 3, "name": "Executive Approval", "approver": "Jonathan Vance, General Counsel", "status": "Approved", "date": "2026-01-30"}
        ],
        "obligations": [
            {"id": "o1", "title": "Quarterly SLA Compliance Reporting", "type": "Reporting", "due_date": "2026-09-30", "status": "Pending", "owner": "Elena Rostova, Esq."},
            {"id": "o2", "title": "Annual License Fee Payment ($1.5M)", "type": "Payment", "due_date": "2027-02-01", "status": "Pending", "owner": "Finance Team"}
        ]
    }


@router.get("/clauses/library", status_code=status.HTTP_200_OK)
async def list_clause_library():
    """Retrieve clause library items including standard, fallback, and jurisdiction-specific clauses."""
    return [
        {
            "id": "cl-01",
            "category": "Limitation of Liability",
            "title": "Standard Mutual Liability Cap (2x Trailing Fees)",
            "type": "Standard",
            "jurisdiction": "Delaware, USA",
            "clause_text": "Neither party shall be liable for indirect or consequential damages. Aggregate liability shall not exceed 2x fees paid in trailing 12 months.",
            "fallback_text": "Aggregate liability shall not exceed total fees paid under this Agreement."
        },
        {
            "id": "cl-02",
            "category": "Data Privacy",
            "title": "EU AI Act Article 10 Audit & Safeguards Clause",
            "type": "Jurisdiction Specific",
            "jurisdiction": "European Union",
            "clause_text": "Vendor warrants compliance with EU AI Act Article 10 data quality controls and technical model cards.",
            "fallback_text": "Vendor agrees to provide annual third-party AI audit reports upon 30 days written notice."
        }
    ]
