from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Court(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "courts"

    name: Mapped[str] = mapped_column(String(255), nullable=False)  # Delaware Court of Chancery, US District Court SDNY, High Court London, etc.
    court_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Chancery, Federal District, Commercial Court, Appellate, Supreme, Arbitration Tribunal
    jurisdiction: Mapped[str] = mapped_column(String(100), nullable=False)  # Delaware, USA, New York, UK, EU, International
    location: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    judges: Mapped[List["Judge"]] = relationship("Judge", back_populates="court")
    cases: Mapped[List["LitigationCase"]] = relationship("LitigationCase", back_populates="court")


class Judge(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "judges"

    name: Mapped[str] = mapped_column(String(255), nullable=False)  # Chancellor Kathaleen St. J. McCormick, Hon. Jed S. Rakoff
    title: Mapped[str] = mapped_column(String(100), default="Judge", nullable=False)
    court_id: Mapped[str] = mapped_column(String(36), ForeignKey("courts.id", ondelete="CASCADE"), nullable=False, index=True)
    biography: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    court: Mapped["Court"] = relationship("Court", back_populates="judges")
    cases: Mapped[List["LitigationCase"]] = relationship("LitigationCase", back_populates="judge")


class LitigationCase(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "litigation_cases"

    case_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # e.g., LIT-2026-089
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Acme Global vs. TechCorp Global Inc.
    case_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Commercial, Employment, Civil, Regulatory, Arbitration, Mediation, IP, Class Action
    
    status: Mapped[str] = mapped_column(String(50), default="Investigation", index=True, nullable=False)
    # Case Intake, Conflict Check, Investigation, Legal Research, Evidence Collection, Discovery, Pre-Trial, Trial, Judgment, Appeal, Settlement, Closed, Archived
    
    risk_level: Mapped[str] = mapped_column(String(20), default="High", nullable=False)  # Low, Medium, High, Critical
    risk_score: Mapped[float] = mapped_column(Float, default=82.5, nullable=False)
    
    claim_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    
    court_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("courts.id", ondelete="SET NULL"), nullable=True, index=True)
    judge_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("judges.id", ondelete="SET NULL"), nullable=True, index=True)
    matter_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("matters.id", ondelete="SET NULL"), nullable=True, index=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    lead_counsel_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    
    filing_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    trial_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    closed_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # AI Intelligence Attributes
    ai_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ai_strategy_recommendation: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    contradiction_alerts_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    # Relationships
    court: Mapped[Optional["Court"]] = relationship("Court", back_populates="cases")
    judge: Mapped[Optional["Judge"]] = relationship("Judge", back_populates="cases")
    evidence_items: Mapped[List["Evidence"]] = relationship("Evidence", back_populates="case", cascade="all, delete-orphan")
    discovery_requests: Mapped[List["DiscoveryRequest"]] = relationship("DiscoveryRequest", back_populates="case", cascade="all, delete-orphan")
    hearings: Mapped[List["Hearing"]] = relationship("Hearing", back_populates="case", cascade="all, delete-orphan")
    filings: Mapped[List["LegalFiling"]] = relationship("LegalFiling", back_populates="case", cascade="all, delete-orphan")
    settlements: Mapped[List["Settlement"]] = relationship("Settlement", back_populates="case", cascade="all, delete-orphan")
    participants: Mapped[List["CaseParticipant"]] = relationship("CaseParticipant", back_populates="case", cascade="all, delete-orphan")


class CaseParticipant(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "case_participants"

    case_id: Mapped[str] = mapped_column(String(36), ForeignKey("litigation_cases.id", ondelete="CASCADE"), nullable=False, index=True)
    participant_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Plaintiff, Defendant, Petitioner, Respondent, External Counsel, Expert Witness, Arbitrator, Mediator
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    role_description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    contact_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    case: Mapped["LitigationCase"] = relationship("LitigationCase", back_populates="participants")


class Evidence(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "evidence"

    case_id: Mapped[str] = mapped_column(String(36), ForeignKey("litigation_cases.id", ondelete="CASCADE"), nullable=False, index=True)
    evidence_number: Mapped[str] = mapped_column(String(50), index=True, nullable=False)  # e.g., EVD-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    evidence_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Document, Image, Video, Audio, Email, Chat Record, Contract, Invoice
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    sha256_hash: Mapped[str] = mapped_column(String(64), nullable=False)  # Immutable Chain of Custody Hash
    custodian_name: Mapped[str] = mapped_column(String(255), nullable=False)
    collected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    admissibility_status: Mapped[str] = mapped_column(String(50), default="Admissible", nullable=False)  # Admissible, Challenged, Suppressed, Pending Review
    ai_contradiction_flag: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    case: Mapped["LitigationCase"] = relationship("LitigationCase", back_populates="evidence_items")


class DiscoveryRequest(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "discovery_requests"

    case_id: Mapped[str] = mapped_column(String(36), ForeignKey("litigation_cases.id", ondelete="CASCADE"), nullable=False, index=True)
    request_number: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., DISC-2026-012
    request_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Document Request, Interrogatory, Deposition, Admission
    propounding_party: Mapped[str] = mapped_column(String(255), nullable=False)
    responding_party: Mapped[str] = mapped_column(String(255), nullable=False)
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Pending", nullable=False)  # Pending, Served, Responded, Objections Filed, Overdue

    case: Mapped["LitigationCase"] = relationship("LitigationCase", back_populates="discovery_requests")


class Hearing(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "hearings"

    case_id: Mapped[str] = mapped_column(String(36), ForeignKey("litigation_cases.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Motion to Dismiss Hearing, Initial Scheduling Conference
    hearing_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Court Hearing, Virtual Hearing, Arbitration Session, Mediation Session
    scheduled_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    court_room: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    virtual_meeting_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="Scheduled", nullable=False)  # Scheduled, In Progress, Completed, Postponed
    outcome_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    case: Mapped["LitigationCase"] = relationship("LitigationCase", back_populates="hearings")


class LegalFiling(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "legal_filings"

    case_id: Mapped[str] = mapped_column(String(36), ForeignKey("litigation_cases.id", ondelete="CASCADE"), nullable=False, index=True)
    filing_number: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., FLG-2026-004
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Motion for Summary Judgment, Complaint
    filing_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Complaint, Answer, Motion, Affidavit, Brief, Court Order, Judgment
    filed_by: Mapped[str] = mapped_column(String(255), nullable=False)
    filing_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Filed", nullable=False)  # Draft, Filed, Granted, Denied, Pending Order

    case: Mapped["LitigationCase"] = relationship("LitigationCase", back_populates="filings")


class Settlement(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "settlements"

    case_id: Mapped[str] = mapped_column(String(36), ForeignKey("litigation_cases.id", ondelete="CASCADE"), nullable=False, index=True)
    offer_amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    offered_by: Mapped[str] = mapped_column(String(255), nullable=False)
    offered_to: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Negotiating", nullable=False)  # Draft, Offered, Counter-Offered, Accepted, Rejected, Executed
    terms_summary: Mapped[str] = mapped_column(Text, nullable=False)
    is_confidential: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    case: Mapped["LitigationCase"] = relationship("LitigationCase", back_populates="settlements")
