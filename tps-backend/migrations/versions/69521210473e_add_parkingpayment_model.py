"""Add ParkingPayment model

Revision ID: 69521210473e
Revises: bc233928ae1d
Create Date: 2025-05-31 14:16:49.523541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69521210473e'
down_revision = 'bc233928ae1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parking_payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('license_plate', sa.String(length=20), nullable=False),
    sa.Column('lot_id', sa.String(length=50), nullable=False),
    sa.Column('payment_type', sa.String(length=50), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('currency', sa.String(length=10), nullable=False),
    sa.Column('external_transaction_id', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('parking_payments', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_parking_payments_external_transaction_id'), ['external_transaction_id'], unique=True)
        batch_op.create_index(batch_op.f('ix_parking_payments_license_plate'), ['license_plate'], unique=False)
        batch_op.create_index(batch_op.f('ix_parking_payments_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('ix_parking_payments_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_payments', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_parking_payments_user_id'))
        batch_op.drop_index(batch_op.f('ix_parking_payments_status'))
        batch_op.drop_index(batch_op.f('ix_parking_payments_license_plate'))
        batch_op.drop_index(batch_op.f('ix_parking_payments_external_transaction_id'))

    op.drop_table('parking_payments')
    # ### end Alembic commands ###
