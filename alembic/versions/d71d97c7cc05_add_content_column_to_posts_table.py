"""add content column to posts table

Revision ID: d71d97c7cc05
Revises: 14f98996629c
Create Date: 2024-12-18 00:00:48.856779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd71d97c7cc05'
down_revision: Union[str, None] = '14f98996629c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
