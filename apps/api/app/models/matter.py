from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin

# Junction Table for Matter Tags
matter_tags_association = Table(
    "matter_tags_association",
    Base.metadata,
    Column("matter_id", String(36), ForeignKey("matters.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", String(36), ForeignKey("matter_tags.id", ondelete="CASCADE"), primary_key=True),
)


class MatterCategory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_categories"

    name: Mapped[str] = mapped_column(String(100), nullable=False)  # Corporate, Employment, Compliance, Regulatory, etc.
    code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    matters: Mapped[List["Matter"]] = relationship("Matter", back_populates="category")


class Matter(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "matters"

    matter_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # e.g., MAT-2026-089
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    category_id: Mapped[str] = mapped_column(String(36), ForeignKey("matter_categories.id", ondelete="RESTRICT"), nullable=False, index=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    department_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    practice_group_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("practice_groups.id", ondelete="SET NULL"), nullable=True)
    
    jurisdiction: Mapped[str] = mapped_column(String(100), default="Delaware, USA", nullable=False)
    
    # State Machine & Lifecycle
    status: Mapped[str] = mapped_column(String(50), default="Active", index=True, nullable=False)
    # Statuses: Draft, Intake, Assigned, Under Review, Active, Waiting, Escalated, Pending Approval, Resolved, Closed, Archived, Cancelled
    
    priority: Mapped[str] = mapped_column(String(20), default="Medium", index=True, nullable=False)  # Low, Medium, High, Critical
    risk_level: Mapped[str] = mapped_column(String(20), default="Medium", index=True, nullable=False)  # Low, Medium, High, Critical
    risk_score: Mapped[float] = mapped_column(Float, default=45.0, nullable=False)  # 0.0 to 100.0
    
    estimated_value: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    currency: Mapped[str] = mapped_column(String(10), default="USD", nullable=False)
    
    opened_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    closed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    target_completion_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # AI Preparation Schemas
    ai_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ai_suggested_actions: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    rag_indexed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    category: Mapped["MatterCategory"] = relationship("MatterCategory", back_populates="matters")
    participants: Mapped[List["MatterParticipant"]] = relationship("MatterParticipant", back_populates="matter", cascade="all, delete-orphan")
    timeline_events: Mapped[List["MatterTimeline"]] = relationship("MatterTimeline", back_populates="matter", cascade="all, delete-orphan")
    tasks: Mapped[List["MatterTask"]] = relationship("MatterTask", back_populates="matter", cascade="all, delete-orphan")
    comments: Mapped[List["MatterComment"]] = relationship("MatterComment", back_populates="matter", cascade="all, delete-orphan")
    tags: Mapped[List["MatterTag"]] = relationship("MatterTag", secondary=matter_tags_association, back_populates="matters")


class MatterParticipant(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_participants"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    # Primary Counsel, Supporting Counsel, Legal Assistant, Compliance Officer, Risk Manager, External Counsel, Reviewer, Approver, Observer

    matter: Mapped["Matter"] = relationship("Matter", back_populates="participants")
    user: Mapped["User"] = relationship("User")


class MatterTimeline(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_timeline"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    # Creation, Assignment, Comment, Approval, StatusChange, DocumentUpload, EvidenceAdded, Meeting, Hearing, AIAnalysis, Notification, AuditEvent
    
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_by_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    matter: Mapped["Matter"] = relationship("Matter", back_populates="timeline_events")
    created_by: Mapped[Optional["User"]] = relationship("User")


class MatterTask(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_tasks"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    owner_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    parent_task_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("matter_tasks.id", ondelete="SET NULL"), nullable=True)
    
    priority: Mapped[str] = mapped_column(String(20), default="Medium", nullable=False)  # Low, Medium, High, Critical
    status: Mapped[str] = mapped_column(String(50), default="To Do", index=True, nullable=False)  # To Do, In Progress, In Review, Completed, Blocked
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    is_recurring: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    matter: Mapped["Matter"] = relationship("Matter", back_populates="tasks")
    owner: Mapped[Optional["User"]] = relationship("User")


class MatterComment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_comments"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    parent_comment_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("matter_comments.id", ondelete="SET NULL"), nullable=True)
    
    is_internal: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_pinned: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_resolved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    attachments_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    matter: Mapped["Matter"] = relationship("Matter", back_populates="comments")
    user: Mapped["User"] = relationship("User")


class MatterTag(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_tags"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    color: Mapped[str] = mapped_column(String(20), default="#3660d8", nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    matters: Mapped[List["Matter"]] = relationship("Matter", secondary=matter_tags_association, back_populates="tags")


class MatterActivity(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_activities"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    details_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)


class MatterRelationship(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_relationships"

    source_matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    target_matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    relationship_type: Mapped[str] = mapped_column(String(50), default="Related", nullable=False)  # Related, Precedent, Parent, Child, Dependent


class MatterFavorite(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_favorites"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)


class MatterWatcher(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "matter_watchers"

    matter_id: Mapped[str] = mapped_column(String(36), ForeignKey("matters.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
