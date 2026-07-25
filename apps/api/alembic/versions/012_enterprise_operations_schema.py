"""012_enterprise_operations_schema

Revision ID: 012_enterprise_operations
Revises: 011_enterprise_integration
Create Date: 2026-07-24 23:55:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '012_enterprise_operations'
down_revision: Union[str, None] = '011_enterprise_integration'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
