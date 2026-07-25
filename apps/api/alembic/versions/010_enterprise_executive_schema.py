"""010_enterprise_executive_schema

Revision ID: 010_enterprise_executive
Revises: 009_enterprise_workflow
Create Date: 2026-07-24 23:35:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '010_enterprise_executive'
down_revision: Union[str, None] = '009_enterprise_workflow'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
