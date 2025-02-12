import logging
from sqlalchemy.orm import Session
from ledger_core.models import LedgerEntry
from ledger_core.operations import BaseLedgerOperation

LEDGER_OPERATION_CONFIG = {
    "DAILY_REWARD": 1,
    "SIGNUP_CREDIT": 3,
    "CREDIT_SPEND": -1,
    "CREDIT_ADD": 10,
    "CONTENT_CREATION": -5,
    "CONTENT_ACCESS": 0,
}

def get_balance(db: Session, owner_id: str) -> int:
    """Returns the current balance of a given owner."""
    total = db.query(
        LedgerEntry.amount
    ).filter(
        LedgerEntry.owner_id == owner_id
    ).all()
    
    return sum(amount for (amount,) in total)

def add_ledger_entry(db: Session, owner_id: str, operation: BaseLedgerOperation, amount: int, nonce: str) -> LedgerEntry:
    """Adds a new ledger entry after validation."""
    logging.info(f"Adding ledger entry: owner_id={owner_id}, operation={operation}, amount={amount}, nonce={nonce}")
    if operation not in LEDGER_OPERATION_CONFIG:
        logging.error(f"Invalid operation: {operation}")
        raise ValueError(f"Invalid operation: {operation}")

    # Check if nonce is already used (to prevent duplicate transactions)
    existing_entry = db.query(LedgerEntry).filter(LedgerEntry.nonce == nonce).first()
    if existing_entry:
        logging.error("Duplicate transaction detected")
        raise ValueError("Duplicate transaction detected")

    # Ensure sufficient balance for negative transactions
    new_balance = get_balance(db, owner_id) + amount
    if new_balance < 0:
        logging.error("Insufficient balance")
        raise ValueError("Insufficient balance")

    # Create and store ledger entry
    entry = LedgerEntry(owner_id=owner_id, operation=operation, amount=amount, nonce=nonce)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    logging.info(f"Ledger entry stored: {entry}")

    return entry