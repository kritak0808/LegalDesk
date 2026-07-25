"""002_enterprise_iam_schema

Revision ID: 002_enterprise_iam
Revises: 001_initial_schema
Create Date: 2026-07-24 22:15:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '002_enterprise_iam'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Upgrade script for IAM schema
    pass


def downgrade() -> None:
    pass
