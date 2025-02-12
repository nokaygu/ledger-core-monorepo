from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from ledger_core.database import Base
from ledger_core.operations import BaseLedgerOperation

class LedgerEntry(Base):
    """Defines the ledger entry database table."""
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(String, nullable=False, index=True)
    operation = Column(Enum(BaseLedgerOperation), nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, unique=True, nullable=False)
    created_on = Column(DateTime, default=func.now(), nullable=False)