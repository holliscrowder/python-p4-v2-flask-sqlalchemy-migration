"""add Department

Revision ID: 817d61274849
Revises: f3f56182e8a3
Create Date: 2024-05-14 12:49:49.640227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '817d61274849'
down_revision = 'f3f56182e8a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
