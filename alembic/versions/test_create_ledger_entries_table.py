from alembic import op
import sqlalchemy as sa
from ledger_core.operations import BaseLedgerOperation

# revision identifiers, used by Alembic.
revision = 'test'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'ledger_entries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('owner_id', sa.String, nullable=False),
        sa.Column('operation', sa.Enum(BaseLedgerOperation), nullable=False),
        sa.Column('amount', sa.Integer, nullable=False),
        sa.Column('nonce', sa.String, nullable=False, unique=True),
        sa.Column('created_on', sa.DateTime, server_default=sa.func.now(), nullable=False),
    )

def downgrade():
    op.drop_table('ledger_entries')