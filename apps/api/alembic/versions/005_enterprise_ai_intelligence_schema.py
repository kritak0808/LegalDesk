"""005_enterprise_ai_intelligence_schema

Revision ID: 005_enterprise_ai_intelligence
Revises: 004_enterprise_clm
Create Date: 2026-07-24 22:45:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '005_enterprise_ai_intelligence'
down_revision: Union[str, None] = '004_enterprise_clm'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
