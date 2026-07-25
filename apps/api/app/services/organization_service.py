from typing import List, Optional, Dict, Any
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.organization import Organization, Department, PracticeGroup, OfficeLocation
from app.core.exceptions import NotFoundException


class OrganizationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_organization_profile(self, org_id: str) -> Organization:
        stmt = select(Organization).where(Organization.id == org_id, Organization.is_deleted == False)
        org = (await self.db.execute(stmt)).scalars().first()
        if not org:
            raise NotFoundException("Organization", org_id)
        return org

    async def update_profile(self, org_id: str, values: Dict[str, Any]) -> Organization:
        org = await self.get_organization_profile(org_id)
        for field, val in values.items():
            if hasattr(org, field) and val is not None:
                setattr(org, field, val)
        await self.db.flush()
        return org

    async def get_subsidiaries(self, parent_id: str) -> List[Organization]:
        stmt = select(Organization).where(Organization.parent_id == parent_id, Organization.is_deleted == False)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())

    async def list_departments(self, org_id: str) -> List[Department]:
        stmt = select(Department).where(Department.organization_id == org_id)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())

    async def list_practice_groups(self, org_id: str) -> List[PracticeGroup]:
        stmt = select(PracticeGroup).where(PracticeGroup.organization_id == org_id)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())

    async def list_offices(self, org_id: str) -> List[OfficeLocation]:
        stmt = select(OfficeLocation).where(OfficeLocation.organization_id == org_id)
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
