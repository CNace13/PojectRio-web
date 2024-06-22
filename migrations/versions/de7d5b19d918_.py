"""empty message

Revision ID: de7d5b19d918
Revises: 04759bce64a7
Create Date: 2023-10-17 18:59:43.334994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de7d5b19d918'
down_revision = '04759bce64a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_group_user', sa.Column('date_expires', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_group_user', 'date_expires')
    # ### end Alembic commands ###
