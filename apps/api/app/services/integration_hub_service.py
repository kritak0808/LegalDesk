from typing import List, Dict, Any
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.integration import Integration


class IntegrationHubService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_connected_apps(self, organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "app_name": "Microsoft 365 (Entra ID, Outlook, Teams, SharePoint)",
                "app_code": "MS-365",
                "category": "Identity & Productivity",
                "status": "Connected & Healthy",
                "auth_type": "OAuth2 / SCIM 2.0",
                "last_sync": "2 mins ago"
            },
            {
                "app_name": "DocuSign Enterprise",
                "app_code": "DOCUSIGN",
                "category": "E-Signature",
                "status": "Connected & Healthy",
                "auth_type": "OAuth2 Webhook",
                "last_sync": "Just now"
            },
            {
                "app_name": "Salesforce CRM Enterprise",
                "app_code": "SALESFORCE",
                "category": "CRM",
                "status": "Connected & Healthy",
                "auth_type": "OAuth2 REST API",
                "last_sync": "10 mins ago"
            },
            {
                "app_name": "Okta Identity Cloud",
                "app_code": "OKTA",
                "category": "Identity SSO",
                "status": "Connected & Healthy",
                "auth_type": "SAML 2.0 / SCIM",
                "last_sync": "5 mins ago"
            }
        ]
