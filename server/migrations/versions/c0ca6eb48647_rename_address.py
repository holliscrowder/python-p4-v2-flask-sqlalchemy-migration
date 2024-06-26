"""rename address

Revision ID: c0ca6eb48647
Revises: f96596d3522b
Create Date: 2024-05-14 12:54:03.691618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0ca6eb48647'
down_revision = 'f96596d3522b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments", "address", new_column_name="location")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("departments", "location", new_column_name="address")
    # ### end Alembic commands ###
