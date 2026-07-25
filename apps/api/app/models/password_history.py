from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class PasswordHistory(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "password_histories"

    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
