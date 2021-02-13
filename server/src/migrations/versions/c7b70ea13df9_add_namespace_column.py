"""Add namespace column

Revision ID: c7b70ea13df9
Revises: b9dcddc9a697
Create Date: 2021-02-11 16:03:34.499750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7b70ea13df9'
down_revision = 'b9dcddc9a697'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('short_link', sa.Column('namespace', sa.String(length=30), nullable=True))
    op.create_index('org_ns_prefix', 'short_link', ['organization', 'namespace', 'shortpath_prefix'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('org_ns_prefix', table_name='short_link')
    op.drop_column('short_link', 'namespace')
    # ### end Alembic commands ###
