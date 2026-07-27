from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
import uuid

class TransactionStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class Transaction(ABC):
    def __init__(self, cust_id: str, teller_id: str, amount: float = 0.0):
        self._txn_id: str = str(uuid.uuid4())
        self._cust_id: str = cust_id
        self._teller_id: str = teller_id
        self._amount: float = amount
        self._timestamp: datetime = datetime.now()
        self._status: TransactionStatus = TransactionStatus.PENDING

    # Read-only properties (No setters to preserve immutability)
    @property
    def txn_id(self) -> str:
        return self._txn_id

    @property
    def cust_id(self) -> str:
        return self._cust_id

    @property
    def teller_id(self) -> str:
        return self._teller_id

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def status(self) -> TransactionStatus:
        return self._status

    @abstractmethod
    def execute(self, account) -> bool:
        """Executes transaction logic against a target account."""
        pass


class DepositTransaction(Transaction):
    def execute(self, account) -> bool:
        try:
            account.credit(self._amount)
            self._status = TransactionStatus.SUCCESS
            return True
        except Exception as e:
            self._status = TransactionStatus.FAILED
            return False


class WithdrawTransaction(Transaction):
    def execute(self, account) -> bool:
        if account.balance < self._amount:
            self._status = TransactionStatus.FAILED
            return False
        
        account.debit(self._amount)
        self._status = TransactionStatus.SUCCESS
        return True