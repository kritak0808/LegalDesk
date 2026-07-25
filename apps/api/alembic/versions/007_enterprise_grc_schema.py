"""007_enterprise_grc_schema

Revision ID: 007_enterprise_grc
Revises: 006_enterprise_litigation
Create Date: 2026-07-24 23:05:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '007_enterprise_grc'
down_revision: Union[str, None] = '006_enterprise_litigation'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
