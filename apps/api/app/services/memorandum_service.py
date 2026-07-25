from typing import List, Dict, Any
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.legal_research import LegalMemorandum


class MemorandumService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_memorandums(self, organization_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "memo_number": "MEMO-2026-004",
                "title": "Enforceability of Consequential Damage Caps in Delaware SaaS Contracts",
                "subject": "Commercial Law & Indemnity Caps",
                "author": "Jonathan Vance, General Counsel",
                "status": "Approved",
                "matter_linked": "MAT-2026-089",
                "contract_linked": "CTR-2026-089"
            }
        ]
