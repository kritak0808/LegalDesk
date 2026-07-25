from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Jurisdiction(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "jurisdictions"

    name: Mapped[str] = mapped_column(String(100), nullable=False)  # Delaware, USA; New York, USA; United Kingdom; European Union; India
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    court_system: Mapped[str] = mapped_column(String(100), nullable=False)  # Delaware State Court System, US Federal Judiciary, Senior Courts of England & Wales
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    sources: Mapped[List["LegalSource"]] = relationship("LegalSource", back_populates="jurisdiction")


class LegalSource(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "legal_sources"

    source_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # e.g., SRC-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Arnold v. Society for Savings, 650 A.2d 1270 (Del. 1994)
    source_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Case Law, Statute, Regulation, Circular, Legal Opinion, Internal Memorandum, Playbook
    citation_string: Mapped[str] = mapped_column(String(255), index=True, nullable=False)  # 650 A.2d 1270 (Del. 1994)
    publication_year: Mapped[int] = mapped_column(Integer, nullable=False)
    jurisdiction_id: Mapped[str] = mapped_column(String(36), ForeignKey("jurisdictions.id", ondelete="RESTRICT"), nullable=False, index=True)
    author_or_court: Mapped[str] = mapped_column(String(255), nullable=False)  # Delaware Supreme Court, US Congress, EU Parliament
    full_text: Mapped[str] = mapped_column(Text, nullable=False)
    authority_score: Mapped[float] = mapped_column(Float, default=98.5, nullable=False)  # 0.0 to 100.0 Authority Rank
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    jurisdiction: Mapped["Jurisdiction"] = relationship("Jurisdiction", back_populates="sources")
    citations: Mapped[List["LegalCitation"]] = relationship("LegalCitation", back_populates="source", cascade="all, delete-orphan")


class LegalCitation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "legal_citations"

    source_id: Mapped[str] = mapped_column(String(36), ForeignKey("legal_sources.id", ondelete="CASCADE"), nullable=False, index=True)
    citation_text: Mapped[str] = mapped_column(String(255), nullable=False)
    target_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Case Law, Statute, Regulation
    is_valid: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    verification_status: Mapped[str] = mapped_column(String(50), default="Verified", nullable=False)

    source: Mapped["LegalSource"] = relationship("LegalSource", back_populates="citations")


class Precedent(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "precedents"

    case_source_id: Mapped[str] = mapped_column(String(36), ForeignKey("legal_sources.id", ondelete="CASCADE"), nullable=False, index=True)
    cited_source_id: Mapped[str] = mapped_column(String(36), ForeignKey("legal_sources.id", ondelete="CASCADE"), nullable=False, index=True)
    treatment: Mapped[str] = mapped_column(String(50), nullable=False)  # Leading, Followed, Distinguished, Overruled, Pending Appeal, Conflicting
    key_holding_summary: Mapped[str] = mapped_column(Text, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class ResearchProject(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "research_projects"

    project_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # RES-2026-089
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Delaware Precedents on Uncapped Liability Clauses
    topic: Mapped[str] = mapped_column(String(100), nullable=False)
    matter_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("matters.id", ondelete="SET NULL"), nullable=True, index=True)
    contract_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="SET NULL"), nullable=True, index=True)
    lead_researcher_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    notebooks: Mapped[List["ResearchNotebook"]] = relationship("ResearchNotebook", back_populates="project", cascade="all, delete-orphan")


class ResearchNotebook(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "research_notebooks"

    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("research_projects.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    project: Mapped["ResearchProject"] = relationship("ResearchProject", back_populates="notebooks")
    entries: Mapped[List["NotebookEntry"]] = relationship("NotebookEntry", back_populates="notebook", cascade="all, delete-orphan")


class NotebookEntry(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "notebook_entries"

    notebook_id: Mapped[str] = mapped_column(String(36), ForeignKey("research_notebooks.id", ondelete="CASCADE"), nullable=False, index=True)
    entry_title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[Text] = mapped_column(Text, nullable=False)
    annotations_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    notebook: Mapped["ResearchNotebook"] = relationship("ResearchNotebook", back_populates="entries")


class LegalMemorandum(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "legal_memorandums"

    memo_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # MEMO-2026-004
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Enforceability of Consequential Damage Caps in Delaware SaaS Contracts
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="Approved", nullable=False)  # Draft, In Review, Approved, Published, Archived
    matter_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("matters.id", ondelete="SET NULL"), nullable=True)
    contract_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    executive_summary: Mapped[Text] = mapped_column(Text, nullable=False)
    legal_analysis: Mapped[Text] = mapped_column(Text, nullable=False)
    conclusion: Mapped[Text] = mapped_column(Text, nullable=False)


class ArgumentNode(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "argument_nodes"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    issue_statement: Mapped[str] = mapped_column(Text, nullable=False)
    argument_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Supporting Authority, Opposing Authority, Counter-Argument, Distinction
    confidence_score: Mapped[float] = mapped_column(Float, default=92.0, nullable=False)
    source_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("legal_sources.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
