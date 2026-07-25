from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class User(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    job_title: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    designation: Mapped[Optional[str]] = mapped_column(String(100), default="Senior Counsel", nullable=True)
    
    # Professional Credentials
    bar_registration_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    jurisdictions: Mapped[Optional[dict]] = mapped_column(JSON, default=lambda: ["Delaware Bar", "New York Bar"], nullable=True)
    
    # Organizational Alignment
    department_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)
    practice_group_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("practice_groups.id", ondelete="SET NULL"), nullable=True)
    office_location_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("office_locations.id", ondelete="SET NULL"), nullable=True)

    # Preferences & Avatar
    avatar_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    preferences: Mapped[Optional[dict]] = mapped_column(JSON, default=lambda: {
        "theme": "dark",
        "language": "en",
        "timezone": "America/New_York",
        "email_notifications": True,
        "inapp_notifications": True,
        "copilot_auto_pin": False
    }, nullable=True)

    # Security & Status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    failed_login_attempts: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    locked_until: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    organizations: Mapped[List["UserOrganization"]] = relationship("UserOrganization", back_populates="user", cascade="all, delete-orphan")
    refresh_tokens: Mapped[List["RefreshToken"]] = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")
    sessions: Mapped[List["UserSession"]] = relationship("UserSession", back_populates="user", cascade="all, delete-orphan")
