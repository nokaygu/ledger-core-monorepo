from enum import Enum

class BaseLedgerOperationMixin:
    """Mixin class for shared ledger operations."""
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

class BaseLedgerOperation(str, Enum):
    """Enum class for shared ledger operations."""
    DAILY_REWARD = BaseLedgerOperationMixin.DAILY_REWARD
    SIGNUP_CREDIT = BaseLedgerOperationMixin.SIGNUP_CREDIT
    CREDIT_SPEND = BaseLedgerOperationMixin.CREDIT_SPEND
    CREDIT_ADD = BaseLedgerOperationMixin.CREDIT_ADD