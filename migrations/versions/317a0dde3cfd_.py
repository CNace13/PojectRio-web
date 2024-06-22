"""empty message

Revision ID: 317a0dde3cfd
Revises: e5873923ddbe
Create Date: 2023-04-06 22:35:44.521319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317a0dde3cfd'
down_revision = 'e5873923ddbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('community', 'desc',
               existing_type=sa.VARCHAR(length=64000),
               type_=sa.String(length=1000),
               existing_nullable=True)
    op.alter_column('gecko_code_tag', 'gecko_code_desc',
               existing_type=sa.VARCHAR(length=64000),
               type_=sa.String(length=1000),
               existing_nullable=True)
    op.alter_column('tag', 'desc',
               existing_type=sa.VARCHAR(length=64000),
               type_=sa.String(length=1000),
               existing_nullable=True)
    op.alter_column('user_group', 'desc',
               existing_type=sa.VARCHAR(length=64000),
               type_=sa.String(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_group', 'desc',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=64000),
               existing_nullable=True)
    op.alter_column('tag', 'desc',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=64000),
               existing_nullable=True)
    op.alter_column('gecko_code_tag', 'gecko_code_desc',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=64000),
               existing_nullable=True)
    op.alter_column('community', 'desc',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=64000),
               existing_nullable=True)
    # ### end Alembic commands ###
