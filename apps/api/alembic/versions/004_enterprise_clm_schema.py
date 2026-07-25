"""004_enterprise_clm_schema

Revision ID: 004_enterprise_clm
Revises: 003_enterprise_matter
Create Date: 2026-07-24 22:35:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '004_enterprise_clm'
down_revision: Union[str, None] = '003_enterprise_matter'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
