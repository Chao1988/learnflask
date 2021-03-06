"""empty message

Revision ID: 912abba4fb9d
Revises: 
Create Date: 2020-09-29 15:45:46.919310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912abba4fb9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
