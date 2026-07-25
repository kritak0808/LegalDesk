from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.repositories.user import UserRepository
from app.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["User Management"])


@router.get("", response_model=List[UserRead], status_code=status.HTTP_200_OK)
async def list_users(skip: int = 0, limit: int = 50, db: AsyncSession = Depends(get_db)):
    """List users in the organization."""
    repo = UserRepository(db)
    return await repo.get_all(skip=skip, limit=limit)
