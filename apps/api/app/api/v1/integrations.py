from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.integration_hub_service import IntegrationHubService
from app.services.email_intelligence_service import EmailIntelligenceService
from app.services.signature_service import SignatureService
from app.services.webhook_service import WebhookService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/integrations", tags=["Enterprise Integrations & Connected Platform"])


@router.get("", status_code=status.HTTP_200_OK)
async def list_connected_apps(
    db: AsyncSession = Depends(get_db),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Retrieve connected enterprise applications (Microsoft 365, DocuSign, Salesforce, Okta)."""
    service = IntegrationHubService(db)
    return await service.list_connected_apps(tenant.tenant_id)


@router.get("/emails", status_code=status.HTTP_200_OK)
async def get_matter_emails(matter_id: str = Query("MAT-2026-089")):
    """Retrieve Outlook/Gmail email threads linked to Matters with AI classification."""
    return await EmailIntelligenceService.get_matter_emails(matter_id)


@router.get("/signatures", status_code=status.HTTP_200_OK)
async def get_signature_envelopes(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve DocuSign/Adobe Sign envelope execution status and audit trails."""
    return await SignatureService.get_envelopes(tenant.tenant_id)


@router.get("/webhooks", status_code=status.HTTP_200_OK)
async def list_webhook_subscriptions(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve active outbound webhook event subscriptions and signing secrets."""
    return await WebhookService.list_subscriptions(tenant.tenant_id)
