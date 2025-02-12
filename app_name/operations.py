from enum import Enum
from ledger_core.operations import BaseLedgerOperationMixin

class AppLedgerOperation(str, Enum):
    DAILY_REWARD = BaseLedgerOperationMixin.DAILY_REWARD
    SIGNUP_CREDIT = BaseLedgerOperationMixin.SIGNUP_CREDIT
    CREDIT_SPEND = BaseLedgerOperationMixin.CREDIT_SPEND
    CREDIT_ADD = BaseLedgerOperationMixin.CREDIT_ADD
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"