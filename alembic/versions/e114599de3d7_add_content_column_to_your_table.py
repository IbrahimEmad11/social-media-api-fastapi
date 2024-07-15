"""add content column to your table

Revision ID: e114599de3d7
Revises: cceb628bcd69
Create Date: 2024-07-15 18:48:52.784365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e114599de3d7'
down_revision: Union[str, None] = 'cceb628bcd69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content", sa.String(), nullable = False))


def downgrade() -> None:
    op.drop_column("posts", "content")
