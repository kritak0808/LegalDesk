from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contract import ContractApproval, ApprovalStep
from app.core.exceptions import NotFoundException


class ApprovalService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_contract_approval(self, contract_id: str) -> Optional[ContractApproval]:
        stmt = select(ContractApproval).where(ContractApproval.contract_id == contract_id)
        return (await self.db.execute(stmt)).scalars().first()

    async def record_approval_step(
        self,
        approval_id: str,
        step_number: int,
        approver_id: str,
        decision: str,  # Approved, Rejected, Revision Required
        comments: Optional[str] = None
    ) -> ApprovalStep:
        stmt = select(ApprovalStep).where(
            ApprovalStep.approval_id == approval_id,
            ApprovalStep.step_number == step_number
        )
        step = (await self.db.execute(stmt)).scalars().first()
        if not step:
            raise NotFoundException("ApprovalStep", f"{approval_id}:step_{step_number}")

        step.status = decision
        step.approver_id = approver_id
        step.decision_at = datetime.now(timezone.utc)
        step.comments = comments
        await self.db.flush()
        return step
