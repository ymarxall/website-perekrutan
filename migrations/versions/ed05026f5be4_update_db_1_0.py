"""update db 1.0

Revision ID: ed05026f5be4
Revises: 
Create Date: 2023-10-20 03:31:48.400998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed05026f5be4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calgot',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama_lengkap', sa.String(length=64), nullable=True),
    sa.Column('nama_panggilan', sa.String(length=64), nullable=True),
    sa.Column('jenis_kelamin', sa.String(length=10), nullable=True),
    sa.Column('nomor_wa', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('alamat', sa.String(length=128), nullable=True),
    sa.Column('kampus', sa.String(length=64), nullable=True),
    sa.Column('foto', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calgot')
    # ### end Alembic commands ###
