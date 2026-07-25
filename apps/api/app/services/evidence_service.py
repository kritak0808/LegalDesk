import hashlib
from typing import List, Optional, Dict, Any
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.litigation import Evidence


class EvidenceService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def log_evidence(
        self,
        case_id: str,
        evidence_number: str,
        title: str,
        evidence_type: str,
        file_path: str,
        custodian_name: str,
        notes: Optional[str] = None
    ) -> Evidence:
        sha256_hash = hashlib.sha256(f"{case_id}:{evidence_number}:{file_path}".encode("utf-8")).hexdigest()

        evidence = Evidence(
            case_id=case_id,
            evidence_number=evidence_number,
            title=title,
            evidence_type=evidence_type,
            file_path=file_path,
            sha256_hash=sha256_hash,
            custodian_name=custodian_name,
            admissibility_status="Admissible",
            ai_contradiction_flag=False,
            notes=notes
        )
        self.db.add(evidence)
        await self.db.flush()
        return evidence

    async def list_case_evidence(self, case_id: str) -> List[Evidence]:
        stmt = select(Evidence).where(Evidence.case_id == case_id).order_by(Evidence.created_at.desc())
        res = await self.db.execute(stmt)
        return list(res.scalars().all())
