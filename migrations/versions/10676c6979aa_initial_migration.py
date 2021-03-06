"""Initial migration

Revision ID: 10676c6979aa
Revises: 2b5357b0145a
Create Date: 2018-06-22 23:39:04.241869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10676c6979aa'
down_revision = '2b5357b0145a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('browse_volumes',
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.Column('update_time', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.String(length=45), nullable=False),
    sa.Column('home_view_total', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('article', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('article', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('catalog', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('catalog', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('comments', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('comments', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('mails', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('mails', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('posts', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('posts', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('roles', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('roles', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('tags', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('tags', sa.Column('update_time', sa.DATETIME(), nullable=True))
    op.add_column('users', sa.Column('create_time', sa.DATETIME(), nullable=True))
    op.add_column('users', sa.Column('update_time', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'update_time')
    op.drop_column('users', 'create_time')
    op.drop_column('tags', 'update_time')
    op.drop_column('tags', 'create_time')
    op.drop_column('roles', 'update_time')
    op.drop_column('roles', 'create_time')
    op.drop_column('posts', 'update_time')
    op.drop_column('posts', 'create_time')
    op.drop_column('mails', 'update_time')
    op.drop_column('mails', 'create_time')
    op.drop_column('comments', 'update_time')
    op.drop_column('comments', 'create_time')
    op.drop_column('catalog', 'update_time')
    op.drop_column('catalog', 'create_time')
    op.drop_column('article', 'update_time')
    op.drop_column('article', 'create_time')
    op.drop_table('browse_volumes')
    # ### end Alembic commands ###
