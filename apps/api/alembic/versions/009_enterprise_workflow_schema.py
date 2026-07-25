"""009_enterprise_workflow_schema

Revision ID: 009_enterprise_workflow
Revises: 008_enterprise_legal_research
Create Date: 2026-07-24 23:25:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '009_enterprise_workflow'
down_revision: Union[str, None] = '008_enterprise_legal_research'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
