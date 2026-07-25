from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Workflow(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "workflows"

    workflow_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # WFK-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # High-Value MSA Contract Approval & Risk Review Workflow
    category: Mapped[str] = mapped_column(String(50), nullable=False)  # Matters, Contracts, Litigation, Compliance, Risk, Policies, Research, Board Governance, AI Reviews
    status: Mapped[str] = mapped_column(String(50), default="Published", nullable=False)  # Draft, Published, Paused, Archived
    current_version: Mapped[str] = mapped_column(String(20), default="1.0", nullable=False)
    node_graph_json: Mapped[dict] = mapped_column(JSON, nullable=False)  # Visual Nodes & Edges layout
    trigger_type: Mapped[str] = mapped_column(String(50), default="Contract Created", nullable=False)  # Contract Created, Matter Created, API, Webhook, Schedule
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    executions: Mapped[List["WorkflowExecution"]] = relationship("WorkflowExecution", back_populates="workflow", cascade="all, delete-orphan")


class WorkflowExecution(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "workflow_executions"

    workflow_id: Mapped[str] = mapped_column(String(36), ForeignKey("workflows.id", ondelete="CASCADE"), nullable=False, index=True)
    execution_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # EXEC-2026-089
    status: Mapped[str] = mapped_column(String(50), default="Running", nullable=False)  # Running, Paused, Completed, Failed, Retrying, Cancelled
    current_node_id: Mapped[str] = mapped_column(String(100), nullable=False)
    target_entity_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)  # Associated Contract ID or Matter ID
    execution_state_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    workflow: Mapped["Workflow"] = relationship("Workflow", back_populates="executions")


class BusinessRule(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "business_rules"

    rule_code: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # RUL-2026-001
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # High Contract Value Executive Routing Rule
    module: Mapped[str] = mapped_column(String(50), nullable=False)  # Contracts, Matters, Litigation, Risk
    conditions_json: Mapped[dict] = mapped_column(JSON, nullable=False)  # e.g., {"field": "total_value", "operator": ">=", "value": 1000000}
    action_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Require Executive Approval, Escalate to GC, Trigger AI Audit
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class WorkflowTask(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "workflow_tasks"

    task_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # TSK-2026-089
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    execution_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("workflow_executions.id", ondelete="CASCADE"), nullable=True, index=True)
    assignee_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    priority: Mapped[str] = mapped_column(String(20), default="High", nullable=False)  # Low, Medium, High, Critical
    status: Mapped[str] = mapped_column(String(50), default="Pending", nullable=False)  # Pending, In Progress, Completed, Escalate
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    sla_hours: Mapped[int] = mapped_column(Integer, default=48, nullable=False)


class SLAConfiguration(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "sla_configurations"

    process_name: Mapped[str] = mapped_column(String(100), nullable=False)  # Contract Review SLA, Dispute Filing SLA
    target_hours: Mapped[int] = mapped_column(Integer, nullable=False)  # Target completion in hours (e.g. 24)
    escalation_user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
