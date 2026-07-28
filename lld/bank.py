from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
import uuid


class TransactionStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Account:
    def __init__(self, account_num: str, owner_id: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._acct_num = account_num
        self._owner_id = owner_id
        self._balance = initial_balance

    @property
    def acct_num(self) -> str:
        return self._acct_num

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @property
    def balance(self) -> float:
        return self._balance

    def credit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Credit amount must be strictly positive.")
        self._balance += amount

    def debit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Debit amount must be strictly positive.")
        if amount > self._balance:
            raise ValueError("Cannot withdraw amount greater than current balance.")
        self._balance -= amount


class Transaction(ABC):
    def __init__(self, cust_id: str, teller_id: str, amount: float = 0.0):
        self._txn_id: str = str(uuid.uuid4())
        self._cust_id: str = cust_id
        self._teller_id: str = teller_id
        self._amount: float = amount
        self._timestamp: datetime = datetime.now()
        self._status: TransactionStatus = TransactionStatus.PENDING

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
    def execute(self, account: Account) -> bool:
        """Executes transaction logic against a target account."""
        pass


class DepositTransaction(Transaction):
    def execute(self, account: Account) -> bool:
        try:
            account.credit(self._amount)
            self._status = TransactionStatus.SUCCESS
            return True
        except ValueError:
            self._status = TransactionStatus.FAILED
            return False


class WithdrawTransaction(Transaction):
    def execute(self, account: Account) -> bool:
        try:
            account.debit(self._amount)
            self._status = TransactionStatus.SUCCESS
            return True
        except ValueError:
            self._status = TransactionStatus.FAILED
            return False

class BankSystem:
    def __init__(self):
        self._accounts: dict[str, Account] = {}
        self._transactions: dict[str, Transaction] = {}

    def create_account(self, acct_num: str, owner_id: str, initial_bal: float = 0.0) -> Account:
        if acct_num in self._accounts:
            raise ValueError(f"Account '{acct_num}' already exists.")
        
        account = Account(acct_num, owner_id, initial_bal)
        self._accounts[acct_num] = account
        return account

    def get_account(self, acct_num: str) -> Account | None:
        return self._accounts.get(acct_num)

    def process_transaction(self, acct_num: str, transaction: Transaction) -> bool:
        """Processes a transaction against an account and records the audit log."""
        account = self.get_account(acct_num)
        if not account:
            raise ValueError(f"Account '{acct_num}' not found.")

        # Execute transaction state logic
        success = transaction.execute(account)

        # Store in transactions ledger regardless of outcome for audit history
        self._transactions[transaction.txn_id] = transaction
        return success

    def get_transaction(self, txn_id: str) -> Transaction | None:
        """Retrieves a past transaction by its UUID."""
        return self._transactions.get(txn_id)

    def get_customer_transactions(self, cust_id: str) -> list[Transaction]:
        """Returns all logged transactions associated with a given customer ID."""
        return [
            txn for txn in self._transactions.values() 
            if txn.cust_id == cust_id
        ]
    
    
        