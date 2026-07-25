from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Integration(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "integrations"

    app_name: Mapped[str] = mapped_column(String(100), nullable=False)  # Microsoft 365, Google Workspace, DocuSign, Salesforce, Okta, Workday
    app_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # Identity, Productivity, E-Signature, CRM, ERP, HR, Webhooks
    icon_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="Connected", nullable=False)  # Connected, Disconnected, Warning, Pending Auth
    auth_type: Mapped[str] = mapped_column(String(50), default="OAuth2", nullable=False)  # OAuth2, SAML, API Key, Webhook
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    connections: Mapped[List["IntegrationConnection"]] = relationship("IntegrationConnection", back_populates="integration", cascade="all, delete-orphan")


class IntegrationConnection(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "integration_connections"

    integration_id: Mapped[str] = mapped_column(String(36), ForeignKey("integrations.id", ondelete="CASCADE"), nullable=False, index=True)
    account_email: Mapped[str] = mapped_column(String(255), nullable=False)
    health_status: Mapped[str] = mapped_column(String(50), default="Healthy", nullable=False)
    last_sync_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    api_call_count_24h: Mapped[int] = mapped_column(Integer, default=1420, nullable=False)

    integration: Mapped["Integration"] = relationship("Integration", back_populates="connections")


class SignatureEnvelope(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "signature_envelopes"

    envelope_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # ENV-2026-089
    provider: Mapped[str] = mapped_column(String(50), default="DocuSign", nullable=False)  # DocuSign, Adobe Sign
    subject: Mapped[str] = mapped_column(String(255), nullable=False)  # Master Services Agreement Signature Request
    status: Mapped[str] = mapped_column(String(50), default="Completed", nullable=False)  # Sent, Delivered, Completed, Declined, Voided
    contract_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="SET NULL"), nullable=True, index=True)
    recipients_json: Mapped[dict] = mapped_column(JSON, nullable=False)  # [{name, email, role, status}]
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class WebhookSubscription(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "webhook_subscriptions"

    target_url: Mapped[str] = mapped_column(String(500), nullable=False)
    events_json: Mapped[dict] = mapped_column(JSON, nullable=False)  # ["matter.created", "contract.signed", "risk.updated"]
    signing_secret: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class APIKey(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "api_keys"

    key_name: Mapped[str] = mapped_column(String(100), nullable=False)  # Enterprise Developer Gateway Key
    key_prefix: Mapped[str] = mapped_column(String(20), nullable=False)  # ld_live_...
    scopes_json: Mapped[dict] = mapped_column(JSON, nullable=False)  # ["read:matters", "write:contracts"]
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
