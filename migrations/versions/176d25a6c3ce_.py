"""empty message

Revision ID: 176d25a6c3ce
Revises: 
Create Date: 2022-09-01 15:51:06.939432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '176d25a6c3ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('grant', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
