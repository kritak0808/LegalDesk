from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class RegulatoryFramework(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "regulatory_frameworks"

    name: Mapped[str] = mapped_column(String(100), nullable=False)  # GDPR, CCPA, HIPAA, SOC 2, ISO 27001, PCI DSS, NIST CSF, NIST AI RMF, DPDP Act, EU AI Act, DORA, SOX, FCPA
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    version: Mapped[str] = mapped_column(String(20), default="2026.1", nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    issuing_body: Mapped[str] = mapped_column(String(100), nullable=False)  # EU Parliament, ISO/IEC, AICPA, NIST, US Congress
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    requirements: Mapped[List["FrameworkRequirement"]] = relationship("FrameworkRequirement", back_populates="framework", cascade="all, delete-orphan")


class FrameworkRequirement(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "framework_requirements"

    framework_id: Mapped[str] = mapped_column(String(36), ForeignKey("regulatory_frameworks.id", ondelete="CASCADE"), nullable=False, index=True)
    article_number: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., Article 10, Control 5.1
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Text] = mapped_column(Text, nullable=False)
    risk_level: Mapped[str] = mapped_column(String(20), default="High", nullable=False)  # Low, Medium, High, Critical

    framework: Mapped["RegulatoryFramework"] = relationship("RegulatoryFramework", back_populates="requirements")


class Policy(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "policies"

    policy_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # POL-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # Corporate, Security, Privacy, HR, Legal, AI Governance
    status: Mapped[str] = mapped_column(String(50), default="Published", nullable=False)  # Draft, Review, Approved, Published, Retired, Archived
    version: Mapped[str] = mapped_column(String(20), default="1.0", nullable=False)
    owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    effective_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    review_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)


class Control(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "controls"

    control_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # CTRL-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    control_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Preventive, Detective, Corrective, Technical, Administrative
    nature: Mapped[str] = mapped_column(String(50), default="Automated", nullable=False)  # Automated, Manual
    status: Mapped[str] = mapped_column(String(50), default="Effective", nullable=False)  # Effective, Partially Effective, Ineffective, Not Tested
    owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    testing_frequency: Mapped[str] = mapped_column(String(50), default="Quarterly", nullable=False)


class ControlTest(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "control_tests"

    control_id: Mapped[str] = mapped_column(String(36), ForeignKey("controls.id", ondelete="CASCADE"), nullable=False, index=True)
    test_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    tester_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    result: Mapped[str] = mapped_column(String(50), nullable=False)  # Pass, Fail, Partial Pass
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class EnterpriseRisk(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "enterprise_risks"

    risk_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # RSK-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # Legal, Financial, Operational, Cyber, Privacy, Compliance, Vendor, AI Risk
    likelihood: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 to 5
    impact: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 to 5
    inherent_score: Mapped[float] = mapped_column(Float, nullable=False)  # Likelihood x Impact
    residual_score: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Mitigated", nullable=False)  # Identified, Assessing, Mitigated, Accepted, Transferred
    owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class Incident(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "incidents"

    incident_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # INC-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # Privacy Breach, Security Incident, Policy Violation, AI Governance Incident
    severity: Mapped[str] = mapped_column(String(20), default="High", nullable=False)  # Low, Medium, High, Critical
    status: Mapped[str] = mapped_column(String(50), default="Investigating", nullable=False)  # Reported, Investigating, Remediating, Closed
    reported_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    root_cause: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class BoardMeeting(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "board_meetings"

    meeting_number: Mapped[str] = mapped_column(String(50), nullable=False)  # BRD-2026-Q1
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    scheduled_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="Scheduled", nullable=False)  # Scheduled, In Session, Adjourned
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    resolutions: Mapped[List["BoardResolution"]] = relationship("BoardResolution", back_populates="meeting", cascade="all, delete-orphan")


class BoardResolution(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "board_resolutions"

    meeting_id: Mapped[str] = mapped_column(String(36), ForeignKey("board_meetings.id", ondelete="CASCADE"), nullable=False, index=True)
    resolution_number: Mapped[str] = mapped_column(String(50), nullable=False)  # RES-2026-004
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    resolution_text: Mapped[Text] = mapped_column(Text, nullable=False)
    votes_for: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    votes_against: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Passed", nullable=False)  # Proposed, Passed, Defeated

    meeting: Mapped["BoardMeeting"] = relationship("BoardMeeting", back_populates="resolutions")


class AIGovernanceRecord(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "ai_governance_records"

    model_name: Mapped[str] = mapped_column(String(255), nullable=False)  # LegalDesk RAG Model v5.0
    risk_classification: Mapped[str] = mapped_column(String(50), default="High Risk (EU AI Act)", nullable=False)
    model_owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    bias_audit_status: Mapped[str] = mapped_column(String(50), default="Passed", nullable=False)
    explainability_score: Mapped[float] = mapped_column(Float, default=96.5, nullable=False)
    human_in_loop_required: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
