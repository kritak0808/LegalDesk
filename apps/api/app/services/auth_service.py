from datetime import datetime, timezone, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.user import UserRepository
from app.core.security import verify_password, hash_password, create_access_token, create_refresh_token
from app.core.exceptions import UnauthorizedException, ValidationException
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.models.user import User
from app.models.organization import Organization, UserOrganization
from app.core.config import settings


class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repo = UserRepository(session)

    async def authenticate_user(self, credentials: LoginRequest) -> TokenResponse:
        user = await self.user_repo.get_by_email(credentials.email)
        if not user or not verify_password(credentials.password, user.hashed_password):
            raise UnauthorizedException("Invalid email or password.")

        if not user.is_active:
            raise UnauthorizedException("User account is deactivated.")

        access_token = create_access_token(subject=user.id)
        refresh_token = create_refresh_token(subject=user.id)

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        )

    async def register_user(self, data: RegisterRequest) -> User:
        existing = await self.user_repo.get_by_email(data.email)
        if existing:
            raise ValidationException(f"User with email '{data.email}' already exists.")

        hashed_pw = hash_password(data.password)
        user = User(
            email=data.email,
            hashed_password=hashed_pw,
            full_name=data.full_name,
            job_title=data.job_title,
        )
        created_user = await self.user_repo.create(user)

        # Create default organization for user
        if data.organization_name:
            slug = data.organization_name.lower().replace(" ", "-")
            org = Organization(name=data.organization_name, slug=slug)
            self.session.add(org)
            await self.session.flush()

            user_org = UserOrganization(
                user_id=created_user.id,
                organization_id=org.id,
                is_default=True
            )
            self.session.add(user_org)

        await self.session.commit()
        return created_user
