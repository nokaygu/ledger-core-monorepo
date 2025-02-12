from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ledger_core.database import get_db
from ledger_core.models import LedgerEntry
from ledger_core.services import get_balance, add_ledger_entry
from ledger_core.operations import BaseLedgerOperation
from pydantic import BaseModel

router = APIRouter()

class LedgerRequest(BaseModel):
    owner_id: str
    operation: BaseLedgerOperation
    amount: int
    nonce: str

@router.get("/ledger/{owner_id}")
def read_ledger(owner_id: str, db: Session = Depends(get_db)):
    """Fetches the current balance of a user."""
    return {"owner_id": owner_id, "balance": get_balance(db, owner_id)}

@router.post("/ledger")
def create_ledger_entry(entry: LedgerRequest, db: Session = Depends(get_db)):
    """Processes a ledger transaction."""
    try:
        ledger_entry = add_ledger_entry(db, entry.owner_id, entry.operation, entry.amount, entry.nonce)
        return {"message": "Transaction successful", "entry": ledger_entry}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))