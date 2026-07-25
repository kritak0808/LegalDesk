from typing import Optional, List
from sqlalchemy import String, Boolean, ForeignKey, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class Organization(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    parent_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="SET NULL"), nullable=True)
    
    # Extended Legal Profile
    legal_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    registration_number: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    tax_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    industry: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    primary_jurisdiction: Mapped[Optional[str]] = mapped_column(String(100), default="Delaware, USA", nullable=True)
    timezone: Mapped[str] = mapped_column(String(50), default="UTC", nullable=False)
    
    # Address & Contact
    address: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    website: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    
    # Branding & Customization
    logo_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    branding: Mapped[Optional[dict]] = mapped_column(JSON, default=lambda: {
        "primary_color": "#2c4cc6",
        "accent_color": "#f59e0b",
        "dark_mode_logo": None
    }, nullable=True)
    
    # Workspace Preferences & Feature Flags
    feature_flags: Mapped[Optional[dict]] = mapped_column(JSON, default=lambda: {
        "ai_redlining": True,
        "eu_ai_act_audit": True,
        "litigation_graph": True,
        "websocket_streaming": True,
        "external_counsel_portal": True
    }, nullable=True)
    
    subscription_tier: Mapped[str] = mapped_column(String(50), default="enterprise", nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="active", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relationships
    parent: Mapped[Optional["Organization"]] = relationship("Organization", remote_side="Organization.id", backref="subsidiaries")
    users: Mapped[List["UserOrganization"]] = relationship("UserOrganization", back_populates="organization", cascade="all, delete-orphan")
    departments: Mapped[List["Department"]] = relationship("Department", back_populates="organization", cascade="all, delete-orphan")
    practice_groups: Mapped[List["PracticeGroup"]] = relationship("PracticeGroup", back_populates="organization", cascade="all, delete-orphan")
    offices: Mapped[List["OfficeLocation"]] = relationship("OfficeLocation", back_populates="organization", cascade="all, delete-orphan")


class Department(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "departments"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    organization: Mapped["Organization"] = relationship("Organization", back_populates="departments")


class PracticeGroup(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "practice_groups"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    organization: Mapped["Organization"] = relationship("Organization", back_populates="practice_groups")


class OfficeLocation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "office_locations"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    is_hq: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)

    organization: Mapped["Organization"] = relationship("Organization", back_populates="offices")


class UserOrganization(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "user_organizations"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    role_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("roles.id", ondelete="SET NULL"), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="organizations")
    organization: Mapped["Organization"] = relationship("Organization", back_populates="users")
    role: Mapped[Optional["Role"]] = relationship("Role")
