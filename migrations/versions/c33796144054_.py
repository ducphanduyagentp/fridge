"""empty message

Revision ID: c33796144054
Revises: 97925bad39df
Create Date: 2021-01-17 17:52:46.363463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c33796144054'
down_revision = '97925bad39df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('ingredient_type', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'ingredient_type')
    # ### end Alembic commands ###
