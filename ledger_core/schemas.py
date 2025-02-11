from pydantic import BaseModel, Field
from datetime import datetime
from ledger_core.operations import BaseLedgerOperation

class LedgerEntry(BaseModel):
    """Schema for validating ledger entries."""
    owner_id: str = Field(..., description="Unique ID of the user")
    operation: BaseLedgerOperation
    amount: int = Field(..., description="Amount of credits")
    nonce: str = Field(..., description="Unique transaction identifier")
    created_on: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the transaction")
