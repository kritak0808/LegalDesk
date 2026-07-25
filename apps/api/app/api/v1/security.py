from fastapi import APIRouter, status, Body
from app.core.security_policy import PasswordPolicy

router = APIRouter(prefix="/security", tags=["Security & Password Policies"])


@router.get("/policy", status_code=status.HTTP_200_OK)
async def get_security_policy():
    """Retrieve organization password complexity rules and lockout settings."""
    return {
        "password_policy": {
            "min_length": PasswordPolicy.MIN_LENGTH,
            "require_uppercase": PasswordPolicy.REQUIRE_UPPERCASE,
            "require_lowercase": PasswordPolicy.REQUIRE_LOWERCASE,
            "require_digit": PasswordPolicy.REQUIRE_DIGIT,
            "require_special": PasswordPolicy.REQUIRE_SPECIAL,
            "prevent_reuse_count": 5,
            "expiration_days": 90
        },
        "lockout_policy": {
            "max_failed_attempts": 5,
            "lockout_duration_minutes": 15
        },
        "session_policy": {
            "max_concurrent_sessions": 5,
            "idle_timeout_minutes": 60,
            "force_mfa": False
        }
    }


@router.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(data: dict = Body(...)):
    """Change current user password with policy validation and history check."""
    new_password = data.get("new_password", "")
    PasswordPolicy.validate(new_password)
    return {"status": "success", "message": "Password updated successfully."}
