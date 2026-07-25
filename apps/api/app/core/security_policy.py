import re
from datetime import datetime, timezone, timedelta
from typing import List, Optional
from app.core.exceptions import ValidationException, LegalDeskException
from app.core.redis import get_redis_client
from app.core.logging import logger


class PasswordPolicy:
    MIN_LENGTH = 10
    REQUIRE_UPPERCASE = True
    REQUIRE_LOWERCASE = True
    REQUIRE_DIGIT = True
    REQUIRE_SPECIAL = True

    @classmethod
    def validate(cls, password: str):
        if len(password) < cls.MIN_LENGTH:
            raise ValidationException(f"Password must be at least {cls.MIN_LENGTH} characters long.")
        if cls.REQUIRE_UPPERCASE and not re.search(r"[A-Z]", password):
            raise ValidationException("Password must contain at least one uppercase letter.")
        if cls.REQUIRE_LOWERCASE and not re.search(r"[a-z]", password):
            raise ValidationException("Password must contain at least one lowercase letter.")
        if cls.REQUIRE_DIGIT and not re.search(r"\d", password):
            raise ValidationException("Password must contain at least one numerical digit.")
        if cls.REQUIRE_SPECIAL and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationException("Password must contain at least one special character.")


class AccountLockoutManager:
    MAX_FAILED_ATTEMPTS = 5
    LOCKOUT_MINUTES = 15

    @classmethod
    def check_lockout(cls, failed_attempts: int, locked_until: Optional[datetime]):
        if locked_until:
            now = datetime.now(timezone.utc)
            if locked_until.tzinfo is None:
                locked_until = locked_until.replace(tzinfo=timezone.utc)
            if now < locked_until:
                diff_secs = int((locked_until - now).total_seconds())
                raise LegalDeskException(
                    message=f"Account is locked due to multiple failed login attempts. Try again in {diff_secs // 60 + 1} minutes.",
                    code="ACCOUNT_LOCKED",
                    status_code=403
                )


async def check_rate_limit(key_prefix: str, identifier: str, max_requests: int = 100, window_seconds: int = 60):
    r = await get_redis_client()
    if r is None:
        return  # Fallback if Redis unavailable
        
    rate_key = f"rate_limit:{key_prefix}:{identifier}"
    current = await r.incr(rate_key)
    if current == 1:
        await r.expire(rate_key, window_seconds)
        
    if current > max_requests:
        logger.warning("rate_limit_exceeded", key=rate_key, current=current, limit=max_requests)
        raise LegalDeskException(
            message="Too many requests. Rate limit exceeded.",
            code="RATE_LIMIT_EXCEEDED",
            status_code=429
        )
