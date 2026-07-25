from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class SystemHealth(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "system_health"

    component_name: Mapped[str] = mapped_column(String(100), nullable=False)  # API Gateway, PostgreSQL, Redis Cache, Celery Workers, WebSockets, OCR Engine
    status: Mapped[str] = mapped_column(String(50), default="Healthy", nullable=False)  # Healthy, Degraded, Critical, Maintenance
    uptime_percentage: Mapped[float] = mapped_column(Float, default=99.99, nullable=False)
    latency_ms: Mapped[float] = mapped_column(Float, default=42.0, nullable=False)
    error_rate_percentage: Mapped[float] = mapped_column(Float, default=0.01, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class InfrastructureMetric(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "infrastructure_metrics"

    metric_name: Mapped[str] = mapped_column(String(100), nullable=False)  # CPU Utilization, Memory Usage, Disk I/O, Network Throughput
    current_value: Mapped[float] = mapped_column(Float, nullable=False)
    target_threshold: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String(20), default="%", nullable=False)
    node_id: Mapped[str] = mapped_column(String(100), default="k8s-worker-node-01", nullable=False)


class SecurityEvent(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "security_events"

    event_type: Mapped[str] = mapped_column(String(100), nullable=False)  # Threat Detected, Permission Violation, Suspicious Login, Rate Limit Exceeded
    severity: Mapped[str] = mapped_column(String(20), default="Medium", nullable=False)  # Low, Medium, High, Critical
    source_ip: Mapped[str] = mapped_column(String(45), nullable=False)  # IPv4/IPv6
    user_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    description: Mapped[Text] = mapped_column(Text, nullable=False)
    action_taken: Mapped[str] = mapped_column(String(100), default="Session Revoked & IP Throttled", nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class JobExecution(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "job_executions"

    job_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # JOB-2026-089
    job_name: Mapped[str] = mapped_column(String(100), nullable=False)  # OCR Text Extraction, RAG Embedding Generator, Nightly Backup
    worker_queue: Mapped[str] = mapped_column(String(50), default="celery-high-priority", nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="Completed", nullable=False)  # Pending, Processing, Completed, Failed, Retrying
    execution_time_ms: Mapped[float] = mapped_column(Float, default=320.0, nullable=False)
    retries_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class BackupJob(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "backup_jobs"

    backup_number: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)  # BKP-2026-089
    backup_type: Mapped[str] = mapped_column(String(50), default="Point-in-Time Database Backup", nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)  # e.g., 4294967296 (4 GB)
    status: Mapped[str] = mapped_column(String(50), default="Verified", nullable=False)  # In Progress, Completed, Verified, Failed
    storage_location: Mapped[str] = mapped_column(String(500), nullable=False)  # s3://legaldesk-backups-us-east-1/bkp-2026-089.enc
    encryption_status: Mapped[str] = mapped_column(String(50), default="AES-256 Encrypted", nullable=False)


class FeatureFlag(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "feature_flags"

    flag_key: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)  # enable_ai_negotiation_v2
    flag_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    rollout_percentage: Mapped[int] = mapped_column(Integer, default=100, nullable=False)  # 0 to 100%
    target_environment: Mapped[str] = mapped_column(String(50), default="Production", nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
