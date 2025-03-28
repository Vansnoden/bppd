"""geometry added to observation

Revision ID: 5d4320602176
Revises: d55d6d7bb5c6
Create Date: 2024-11-25 21:05:59.163716

"""
from typing import Sequence, Union

from alembic import op
import geoalchemy2
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5d4320602176'
down_revision: Union[str, None] = 'd55d6d7bb5c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('observations', sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT', from_text='ST_GeomFromEWKT', name='geometry', nullable=True), nullable=True))
    op.alter_column('observations', 'lat',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('observations', 'lon',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    #op.create_index('idx_observations_geom', 'observations', ['geom'], unique=False, postgresql_using='gist')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_observations_geom', table_name='observations', postgresql_using='gist')
    op.alter_column('observations', 'lon',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('observations', 'lat',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.drop_column('observations', 'geom')
    
