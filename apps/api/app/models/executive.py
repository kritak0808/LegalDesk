from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class ExecutiveDashboard(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "executive_dashboards"

    dashboard_name: Mapped[str] = mapped_column(String(100), nullable=False)  # Executive Command Center, General Counsel Studio, Board View
    enterprise_health_score: Mapped[float] = mapped_column(Float, default=96.4, nullable=False)
    compliance_score: Mapped[float] = mapped_column(Float, default=98.2, nullable=False)
    risk_index_score: Mapped[float] = mapped_column(Float, default=18.5, nullable=False)  # Lower is safer
    outside_counsel_spend_usd: Mapped[float] = mapped_column(Float, default=14200000.0, nullable=False)
    litigation_exposure_usd: Mapped[float] = mapped_column(Float, default=84500000.0, nullable=False)
    board_readiness_status: Mapped[str] = mapped_column(String(50), default="Board Ready", nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    metrics: Mapped[List["ExecutiveMetric"]] = relationship("ExecutiveMetric", back_populates="dashboard", cascade="all, delete-orphan")


class ExecutiveMetric(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "executive_metrics"

    dashboard_id: Mapped[str] = mapped_column(String(36), ForeignKey("executive_dashboards.id", ondelete="CASCADE"), nullable=False, index=True)
    metric_name: Mapped[str] = mapped_column(String(100), nullable=False)  # Legal Efficiency Score, Contract Velocity, Matter Throughput
    current_value: Mapped[float] = mapped_column(Float, nullable=False)
    previous_value: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String(20), default="%", nullable=False)
    status_indicator: Mapped[str] = mapped_column(String(20), default="Optimal", nullable=False)  # Optimal, Warning, Critical

    dashboard: Mapped["ExecutiveDashboard"] = relationship("ExecutiveDashboard", back_populates="metrics")


class LegalSpend(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "legal_spends"

    firm_name: Mapped[str] = mapped_column(String(255), nullable=False)  # Wachtell, Lipton, Rosen & Katz; Latham & Watkins; Skadden Arps
    practice_area: Mapped[str] = mapped_column(String(100), nullable=False)  # M&A, Commercial Litigation, Regulatory Defense, IP
    billing_model: Mapped[str] = mapped_column(String(50), default="Hourly + AFA", nullable=False)
    total_billed_usd: Mapped[float] = mapped_column(Float, nullable=False)
    budget_allocated_usd: Mapped[float] = mapped_column(Float, nullable=False)
    billing_accuracy_score: Mapped[float] = mapped_column(Float, default=99.4, nullable=False)
    win_rate_percentage: Mapped[float] = mapped_column(Float, default=88.5, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class Forecast(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "forecasts"

    forecast_type: Mapped[str] = mapped_column(String(100), nullable=False)  # Litigation Settlement Probability, Budget Overrun Risk, Contract Delay
    target_entity_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    predicted_probability: Mapped[float] = mapped_column(Float, default=78.4, nullable=False)
    confidence_level: Mapped[float] = mapped_column(Float, default=94.0, nullable=False)
    forecast_details_json: Mapped[dict] = mapped_column(JSON, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class BoardReport(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "board_reports"

    report_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # BRD-REP-2026-Q1
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Q1 2026 Enterprise Legal, Regulatory Risk & Board Briefing
    period: Mapped[str] = mapped_column(String(50), default="Q1 2026", nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Finalized", nullable=False)  # Draft, Finalized, Presented
    prepared_by_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    executive_summary: Mapped[Text] = mapped_column(Text, nullable=False)
    pdf_export_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
