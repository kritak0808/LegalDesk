"""003_enterprise_matter_schema

Revision ID: 003_enterprise_matter
Revises: 002_enterprise_iam
Create Date: 2026-07-24 22:25:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '003_enterprise_matter'
down_revision: Union[str, None] = '002_enterprise_iam'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
