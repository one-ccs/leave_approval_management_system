"""user 表添加手机号，admin、assistant 删除手机号

Revision ID: 68f506f50d7f
Revises: fca0f1613387
Create Date: 2024-05-25 03:37:16.491468

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '68f506f50d7f'
down_revision = 'fca0f1613387'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_column('telephone')

    with op.batch_alter_table('assistant', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               comment='辅导员 id',
               existing_comment='教师 id',
               existing_nullable=False,
               autoincrement=True)
        batch_op.drop_column('telephone')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telephone', sa.String(length=11), nullable=True, comment='电话号码'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('telephone')

    with op.batch_alter_table('assistant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telephone', mysql.VARCHAR(length=11), nullable=True, comment='电话号码'))
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               comment='教师 id',
               existing_comment='辅导员 id',
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telephone', mysql.VARCHAR(length=11), nullable=True, comment='电话号码'))

    # ### end Alembic commands ###
