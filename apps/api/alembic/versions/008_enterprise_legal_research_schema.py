"""008_enterprise_legal_research_schema

Revision ID: 008_enterprise_legal_research
Revises: 007_enterprise_grc
Create Date: 2026-07-24 23:15:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '008_enterprise_legal_research'
down_revision: Union[str, None] = '007_enterprise_grc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
