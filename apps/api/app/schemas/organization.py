from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class OrganizationCreate(BaseModel):
    name: str
    slug: str
    industry: Optional[str] = "Legal Services"
    subscription_tier: Optional[str] = "enterprise"


class OrganizationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    slug: str
    industry: Optional[str]
    subscription_tier: str
    is_active: bool
    created_at: datetime
