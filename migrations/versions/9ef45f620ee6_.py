"""empty message

Revision ID: 9ef45f620ee6
Revises: 6279201594b8
Create Date: 2019-10-28 16:51:19.859290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ef45f620ee6'
down_revision = '6279201594b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data', sa.Column('url', sa.String(length=120), nullable=True))
    op.drop_column('data', 'url1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data', sa.Column('url1', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('data', 'url')
    # ### end Alembic commands ###
