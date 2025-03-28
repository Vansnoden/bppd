"""year field added to observation table

Revision ID: 9980f82fba9d
Revises: d860195eb721
Create Date: 2024-11-25 18:20:34.346950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9980f82fba9d'
down_revision: Union[str, None] = 'd860195eb721'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('observations', sa.Column('year', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('observations', 'year')
    # ### end Alembic commands ###
