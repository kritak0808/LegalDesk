from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class ContractType(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_types"

    name: Mapped[str] = mapped_column(String(100), nullable=False)  # NDA, MSA, SOW, Employment, Vendor, Procurement, Licensing, DPA, M&A, etc.
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    contracts: Mapped[List["Contract"]] = relationship("Contract", back_populates="contract_type")


class Contract(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "contracts"

    contract_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # e.g., CTR-2026-089
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    contract_type_id: Mapped[str] = mapped_column(String(36), ForeignKey("contract_types.id", ondelete="RESTRICT"), nullable=False, index=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    matter_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("matters.id", ondelete="SET NULL"), nullable=True, index=True)
    department_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    
    jurisdiction: Mapped[str] = mapped_column(String(100), default="Delaware, USA", nullable=False)
    governing_law: Mapped[str] = mapped_column(String(100), default="Delaware State Law", nullable=False)
    
    # State Machine Lifecycle
    status: Mapped[str] = mapped_column(String(50), default="Active", index=True, nullable=False)
    # Request, Draft, Internal Review, Legal Review, Business Review, Negotiation, Pending Approval, Approved, Ready for Signature, Executed, Active, Expired, Renewal Pending, Renewed, Terminated, Archived
    
    risk_level: Mapped[str] = mapped_column(String(20), default="Medium", index=True, nullable=False)  # Low, Medium, High, Critical
    deviation_score: Mapped[float] = mapped_column(Float, default=15.0, nullable=False)  # 0.0 to 100.0 deviation from standard playbook
    
    total_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    annual_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    
    effective_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    expiration_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    signed_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    
    # Renewal Management Attributes
    auto_renew: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    renewal_notice_days: Mapped[int] = mapped_column(Integer, default=60, nullable=False)  # Days before expiration to give notice
    renewal_status: Mapped[str] = mapped_column(String(50), default="None", nullable=False)  # None, Notice Pending, Renewed, Terminated

    # AI Preparation Attributes
    ai_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    clause_risk_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    suggested_clauses_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    missing_clauses_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    similarity_index: Mapped[Optional[float]] = mapped_column(Float, default=94.2, nullable=True)

    # Relationships
    contract_type: Mapped["ContractType"] = relationship("ContractType", back_populates="contracts")
    parties: Mapped[List["ContractParty"]] = relationship("ContractParty", back_populates="contract", cascade="all, delete-orphan")
    versions: Mapped[List["ContractVersion"]] = relationship("ContractVersion", back_populates="contract", cascade="all, delete-orphan")
    approvals: Mapped[List["ContractApproval"]] = relationship("ContractApproval", back_populates="contract", cascade="all, delete-orphan")
    obligations: Mapped[List["ContractObligation"]] = relationship("ContractObligation", back_populates="contract", cascade="all, delete-orphan")
    renewals: Mapped[List["ContractRenewal"]] = relationship("ContractRenewal", back_populates="contract", cascade="all, delete-orphan")


class ContractParty(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_parties"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    party_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Internal Entity, Customer, Vendor, Supplier, Government, Partner, External Counsel, Subsidiary
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    signatory_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    signatory_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    jurisdiction: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    tax_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    contract: Mapped["Contract"] = relationship("Contract", back_populates="parties")


class ContractVersion(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_versions"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    version_number: Mapped[str] = mapped_column(String(20), nullable=False)  # e.g., v1.0, v1.1, v2.0
    is_major: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    diff_hash: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    author_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    summary_of_changes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    approval_status: Mapped[str] = mapped_column(String(50), default="Draft", nullable=False)

    contract: Mapped["Contract"] = relationship("Contract", back_populates="versions")
    author: Mapped[Optional["User"]] = relationship("User")


class ClauseCategory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "clause_categories"

    name: Mapped[str] = mapped_column(String(100), nullable=False)  # Indemnity, Limitation of Liability, Termination, IP, Confidentiality, Governing Law
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    clauses: Mapped[List["ClauseLibrary"]] = relationship("ClauseLibrary", back_populates="category")


class ClauseLibrary(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "clause_library"

    category_id: Mapped[str] = mapped_column(String(36), ForeignKey("clause_categories.id", ondelete="RESTRICT"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    clause_text: Mapped[str] = mapped_column(Text, nullable=False)
    fallback_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    clause_type: Mapped[str] = mapped_column(String(50), default="Standard", nullable=False)  # Standard, Fallback, High Risk, Jurisdiction Specific
    jurisdiction: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_approved: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    category: Mapped["ClauseCategory"] = relationship("ClauseCategory", back_populates="clauses")


class ContractTemplate(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_templates"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    contract_type_id: Mapped[str] = mapped_column(String(36), ForeignKey("contract_types.id", ondelete="RESTRICT"), nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    version: Mapped[str] = mapped_column(String(20), default="1.0", nullable=False)
    template_body: Mapped[str] = mapped_column(Text, nullable=False)
    dynamic_variables_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)  # e.g., ["{{PartyName}}", "{{EffectiveDate}}", "{{FeeAmount}}"]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class ContractApproval(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_approvals"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    current_step: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Pending", nullable=False)  # Pending, Approved, Rejected, Revision Required

    contract: Mapped["Contract"] = relationship("Contract", back_populates="approvals")
    steps: Mapped[List["ApprovalStep"]] = relationship("ApprovalStep", back_populates="approval", cascade="all, delete-orphan")


class ApprovalStep(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "approval_steps"

    approval_id: Mapped[str] = mapped_column(String(36), ForeignKey("contract_approvals.id", ondelete="CASCADE"), nullable=False, index=True)
    step_number: Mapped[int] = mapped_column(Integer, nullable=False)
    step_name: Mapped[str] = mapped_column(String(100), nullable=False)  # Requester, Legal Review, Finance Review, Executive Review, Board Approval
    approver_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="Pending", nullable=False)  # Pending, Approved, Rejected
    decision_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    comments: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    approval: Mapped["ContractApproval"] = relationship("ContractApproval", back_populates="steps")
    approver: Mapped[Optional["User"]] = relationship("User")


class ContractObligation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_obligations"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    obligation_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Payment, Delivery, Notice, Reporting, Compliance, Renewal, Milestone
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    priority: Mapped[str] = mapped_column(String(20), default="Medium", nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Pending", nullable=False)  # Pending, Fulfilled, Overdue, Waived

    contract: Mapped["Contract"] = relationship("Contract", back_populates="obligations")
    owner: Mapped[Optional["User"]] = relationship("User")


class ContractRenewal(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_renewals"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    renewal_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notice_deadline: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    is_auto_renewal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Notice Pending", nullable=False)  # Notice Pending, Renewed, Terminated, Expired
    action_by_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    contract: Mapped["Contract"] = relationship("Contract", back_populates="renewals")


class ContractActivity(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_activities"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    details_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)


class ContractAttachment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "contract_attachments"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(String(50), nullable=False)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
