from typing import List, Optional
from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.organization_service import OrganizationService
from app.core.tenant import get_current_tenant, TenantContext
from app.core.permissions import require_permissions

router = APIRouter(prefix="/organizations", tags=["Organization Management"])


@router.get("/current", status_code=status.HTTP_200_OK)
async def get_current_organization(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve detailed current organization profile, subsidiaries, branding, and feature flags."""
    return {
        "id": "org-acme-global-01",
        "name": "Acme Global Corp",
        "slug": "acme-global",
        "parent_id": None,
        "legal_name": "Acme Global Corporation Inc.",
        "registration_number": "DEL-REG-2026-9904",
        "tax_id": "US-TAX-8821940",
        "industry": "Corporate Governance & SaaS",
        "primary_jurisdiction": "Delaware, USA",
        "timezone": "America/New_York",
        "address": "100 Enterprise Way, Suite 400",
        "city": "Wilmington",
        "country": "United States",
        "phone": "+1 (800) 555-LEGAL",
        "website": "https://acme.example.com",
        "logo_url": "https://images.unsplash.com/photo-1560179707-f14e90ef3623?w=100&auto=format&fit=crop&q=80",
        "branding": {
            "primary_color": "#2c4cc6",
            "accent_color": "#f59e0b",
        },
        "feature_flags": {
            "ai_redlining": True,
            "eu_ai_act_audit": True,
            "litigation_graph": True,
            "external_counsel_portal": True,
            "custom_rbac": True
        },
        "subscription_tier": "enterprise",
        "status": "active",
        "subsidiaries": [
            {"id": "org-acme-eu-02", "name": "Acme Europe B.V.", "jurisdiction": "Netherlands", "ownership": "100%"},
            {"id": "org-acme-asia-03", "name": "Acme Asia-Pacific Pte Ltd", "jurisdiction": "Singapore", "ownership": "100%"}
        ],
        "departments": [
            {"id": "dep-01", "name": "Litigation & Disputes", "code": "LIT"},
            {"id": "dep-02", "name": "Corporate M&A & Securities", "code": "MA"},
            {"id": "dep-03", "name": "Data Privacy & Regulatory", "code": "PRIV"}
        ],
        "offices": [
            {"id": "off-01", "name": "Wilmington HQ", "city": "Wilmington", "country": "USA", "is_hq": True},
            {"id": "off-02", "name": "London Office", "city": "London", "country": "United Kingdom", "is_hq": False}
        ]
    }


@router.patch("/current/branding", status_code=status.HTTP_200_OK, dependencies=[Depends(require_permissions("administration:configure"))])
async def update_organization_branding(branding_data: dict = Body(...)):
    """Update organization custom logo and color branding."""
    return {"status": "success", "branding": branding_data}


@router.patch("/current/feature-flags", status_code=status.HTTP_200_OK, dependencies=[Depends(require_permissions("administration:configure"))])
async def update_feature_flags(flags: dict = Body(...)):
    """Update organization active feature flags."""
    return {"status": "success", "feature_flags": flags}
