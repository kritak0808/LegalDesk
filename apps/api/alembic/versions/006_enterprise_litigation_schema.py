"""006_enterprise_litigation_schema

Revision ID: 006_enterprise_litigation
Revises: 005_enterprise_ai_intelligence
Create Date: 2026-07-24 22:55:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '006_enterprise_litigation'
down_revision: Union[str, None] = '005_enterprise_ai_intelligence'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
