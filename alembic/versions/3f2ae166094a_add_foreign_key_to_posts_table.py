"""add foreign key to posts table

Revision ID: 3f2ae166094a
Revises: a7ee50968b6a
Create Date: 2024-07-15 19:01:47.441105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f2ae166094a'
down_revision: Union[str, None] = 'a7ee50968b6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.Integer(),nullable = False))
    op.create_foreign_key('posts_users_fk',source_table="posts",referent_table="users",local_cols=['user_id'],remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name="posts")
    op.drop_column("user_id")
