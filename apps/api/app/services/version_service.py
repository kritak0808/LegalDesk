import hashlib
from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contract import ContractVersion


class VersionService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_version(
        self,
        contract_id: str,
        version_number: str,
        file_name: str,
        file_path: str,
        author_id: Optional[str] = None,
        summary_of_changes: Optional[str] = None,
        is_major: bool = True
    ) -> ContractVersion:
        diff_hash = hashlib.sha256(f"{contract_id}:{version_number}:{file_name}".encode("utf-8")).hexdigest()

        version = ContractVersion(
            contract_id=contract_id,
            version_number=version_number,
            file_name=file_name,
            file_path=file_path,
            diff_hash=diff_hash,
            author_id=author_id,
            summary_of_changes=summary_of_changes,
            is_major=is_major,
            approval_status="Draft"
        )
        self.db.add(version)
        await self.db.flush()
        return version

    async def get_contract_versions(self, contract_id: str) -> List[ContractVersion]:
        stmt = select(ContractVersion).where(ContractVersion.contract_id == contract_id).order_by(ContractVersion.created_at.desc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
