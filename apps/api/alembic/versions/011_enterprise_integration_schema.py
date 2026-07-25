"""011_enterprise_integration_schema

Revision ID: 011_enterprise_integration
Revises: 010_enterprise_executive
Create Date: 2026-07-24 23:45:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '011_enterprise_integration'
down_revision: Union[str, None] = '010_enterprise_executive'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
