import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ledger_core.database import get_db
from ledger_core.models import LedgerEntry
from ledger_core.services import get_balance, add_ledger_entry
from app_name.operations import AppLedgerOperation
from pydantic import BaseModel

router = APIRouter()

class LedgerRequest(BaseModel):
    owner_id: str
    operation: AppLedgerOperation
    amount: int
    nonce: str

@router.get("/ledger/{owner_id}")
def read_ledger(owner_id: str, db: Session = Depends(get_db)):
    """Fetches the current balance of a user."""
    return {"owner_id": owner_id, "balance": get_balance(db, owner_id)}

@router.post("/ledger")
def create_ledger_entry(entry: LedgerRequest, db: Session = Depends(get_db)):
    """Processes a ledger transaction."""
    logging.info(f"Received ledger entry request: {entry}")
    try:
        ledger_entry = add_ledger_entry(db, entry.owner_id, entry.operation, entry.amount, entry.nonce)
        logging.info(f"Ledger entry created: {ledger_entry}")
        return {"message": "Transaction successful", "entry": ledger_entry}
    except ValueError as e:
        logging.error(f"Error creating ledger entry: {e}")
        raise HTTPException(status_code=400, detail=str(e))