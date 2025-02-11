from enum import Enum

class BaseLedgerOperation(str, Enum):
    """Defines shared ledger operations required by all applications."""
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

def create_app_specific_operations(*operations: str):
    """Helper function to extend BaseLedgerOperation with app-specific operations."""
    return Enum("AppLedgerOperation", {op: op for op in BaseLedgerOperation} | {op: op for op in operations})
