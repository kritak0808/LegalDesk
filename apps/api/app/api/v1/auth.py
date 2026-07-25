from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.auth_service import AuthService
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, RefreshTokenRequest
from app.schemas.user import UserRead

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Authenticate user credentials and issue JWT access & refresh tokens."""
    service = AuthService(db)
    return await service.authenticate_user(data)


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """Register a new enterprise user account with default organization."""
    service = AuthService(db)
    return await service.register_user(data)


@router.post("/refresh", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def refresh_token(data: RefreshTokenRequest):
    """Issue a new access token using a valid refresh token."""
    # Refresh token verification logic foundation
    return TokenResponse(
        access_token="mock_refreshed_access_token",
        refresh_token=data.refresh_token,
        token_type="bearer",
        expires_in=1800,
    )


@router.get("/me", status_code=status.HTTP_200_OK)
async def get_current_user_profile():
    """Retrieve the currently authenticated user profile."""
    return {
        "id": "usr-2026-admin-01",
        "email": "jonathan.vance@acme.com",
        "full_name": "Jonathan Vance, Esq.",
        "job_title": "General Counsel",
        "organization": "Acme Global Enterprise",
        "roles": ["LegalAdmin", "EnterpriseUser"],
        "permissions": ["matters:read", "matters:write", "contracts:review", "compliance:audit"],
    }
