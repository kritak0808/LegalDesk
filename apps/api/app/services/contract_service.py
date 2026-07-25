import uuid
from datetime import datetime, timezone
from typing import List, Optional, Dict, Any
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.contract import Contract, ContractVersion, ContractActivity
from app.core.exceptions import NotFoundException, ValidationException


class ContractService:
    VALID_STATUSES = [
        "Request", "Draft", "Internal Review", "Legal Review", "Business Review",
        "Negotiation", "Pending Approval", "Approved", "Ready for Signature",
        "Executed", "Active", "Expired", "Renewal Pending", "Renewed",
        "Terminated", "Archived"
    ]

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_contract_by_id(self, contract_id: str, organization_id: str) -> Contract:
        stmt = select(Contract).where(
            Contract.id == contract_id,
            Contract.organization_id == organization_id,
            Contract.is_deleted == False
        )
        contract = (await self.db.execute(stmt)).scalars().first()
        if not contract:
            raise NotFoundException("Contract", contract_id)
        return contract

    async def transition_status(self, contract_id: str, organization_id: str, new_status: str, user_id: str) -> Contract:
        if new_status not in self.VALID_STATUSES:
            raise ValidationException(f"Invalid status '{new_status}'. Allowed: {', '.join(self.VALID_STATUSES)}")

        contract = await self.get_contract_by_id(contract_id, organization_id)
        old_status = contract.status
        contract.status = new_status

        if new_status == "Executed":
            contract.signed_date = datetime.now(timezone.utc)

        activity = ContractActivity(
            contract_id=contract.id,
            user_id=user_id,
            action="CONTRACT.STATUS_CHANGED",
            details_json={"from": old_status, "to": new_status}
        )
        self.db.add(activity)
        await self.db.flush()
        return contract
