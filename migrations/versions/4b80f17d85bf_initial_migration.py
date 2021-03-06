"""Initial migration

Revision ID: 4b80f17d85bf
Revises: 2dd682ea280d
Create Date: 2018-06-23 15:25:17.094257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b80f17d85bf'
down_revision = '2dd682ea280d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('birthday', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('full_name', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('gender', sa.String(length=10), nullable=True))
    op.add_column('users', sa.Column('nick_name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'nick_name')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'full_name')
    op.drop_column('users', 'birthday')
    op.drop_column('users', 'address')
    # ### end Alembic commands ###
