from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
import random
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

    def get_transaction_description(self) -> str:
        """Returns formatted string representation for transaction logs."""
        return (
            f"[{self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
            f"ID: {self._txn_id[:8]}... | Type: {self.__class__.__name__:<18} | "
            f"Cust: {self._cust_id} | Teller: {self._teller_id} | "
            f"Amount: ${self._amount:>7.2f} | Status: {self._status.value}"
        )


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

        success = transaction.execute(account)
        self._transactions[transaction.txn_id] = transaction
        return success

    def get_transaction(self, txn_id: str) -> Transaction | None:
        return self._transactions.get(txn_id)

    def get_all_transactions(self) -> list[Transaction]:
        """Returns all recorded transactions across the system."""
        return list(self._transactions.values())

    def get_customer_transactions(self, cust_id: str) -> list[Transaction]:
        return [txn for txn in self._transactions.values() if txn.cust_id == cust_id]


class BankTeller:
    def __init__(self, teller_id: str):
        self._id = teller_id

    @property
    def id(self) -> str:
        return self._id


class BankBranch:
    def __init__(self, address: str, bank_system: BankSystem, initial_cash: float = 0.0):
        self._address = address
        self._bank_system = bank_system
        self._cash_on_hand = initial_cash
        self._tellers: list[BankTeller] = []

    def add_teller(self, teller: BankTeller) -> None:
        self._tellers.append(teller)

    def _get_available_teller_id(self) -> str:
        if not self._tellers:
            raise ValueError("Branch does not have any active tellers.")
        return random.choice(self._tellers).id

    def open_account(self, acct_num: str, customer_id: str, initial_bal: float = 0.0) -> Account:
        _ = self._get_available_teller_id()
        return self._bank_system.create_account(acct_num, customer_id, initial_bal)

    def deposit(self, acct_num: str, customer_id: str, amount: float) -> bool:
        teller_id = self._get_available_teller_id()
        deposit_txn = DepositTransaction(cust_id=customer_id, teller_id=teller_id, amount=amount)
        success = self._bank_system.process_transaction(acct_num, deposit_txn)
        if success:
            self._cash_on_hand += amount
        return success

    def withdraw(self, acct_num: str, customer_id: str, amount: float) -> bool:
        if amount > self._cash_on_hand:
            raise ValueError("Branch does not have sufficient physical cash on hand.")

        teller_id = self._get_available_teller_id()
        withdraw_txn = WithdrawTransaction(cust_id=customer_id, teller_id=teller_id, amount=amount)
        success = self._bank_system.process_transaction(acct_num, withdraw_txn)
        if success:
            self._cash_on_hand -= amount
        return success

    def collect_cash(self, ratio: float) -> float:
        if not (0.0 < ratio <= 1.0):
            raise ValueError("Ratio must be between 0 and 1.")
        cash_to_collect = round(self._cash_on_hand * ratio, 2)
        self._cash_on_hand -= cash_to_collect
        return cash_to_collect

    def provide_cash(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")
        self._cash_on_hand += amount


class Bank:
    def __init__(self, bank_system: BankSystem, initial_vault_cash: float = 0.0):
        self._branches: list[BankBranch] = []
        self._bank_system = bank_system
        self._total_cash = initial_vault_cash

    @property
    def total_cash(self) -> float:
        return self._total_cash

    def add_branch(self, address: str, initial_funds: float = 0.0) -> BankBranch:
        branch = BankBranch(address, self._bank_system, initial_funds)
        self._branches.append(branch)
        self._total_cash += initial_funds
        return branch

    def collect_cash(self, ratio: float) -> float:
        total_collected = 0.0
        for branch in self._branches:
            total_collected += branch.collect_cash(ratio)
        self._total_cash += total_collected
        return total_collected

    def print_transactions(self) -> None:
        transactions = self._bank_system.get_all_transactions()
        if not transactions:
            print("No transactions recorded.")
            return

        print("\n=== System Transaction Ledger ===")
        for transaction in transactions:
            print(transaction.get_transaction_description())


if __name__ == "__main__":
    # Setup Bank System and Bank Enterprise
    system = BankSystem()
    central_bank = Bank(bank_system=system, initial_vault_cash=100000.0)

    # Add Branch & Tellers
    branch_1 = central_bank.add_branch("100 Wall Street", initial_funds=10000.0)
    branch_1.add_teller(BankTeller("T_101"))

    # Open Account & Perform Operations
    account = branch_1.open_account("ACC_001", "CUST_88", initial_bal=500.0)
    branch_1.deposit("ACC_001", "CUST_88", 250.0)
    branch_1.withdraw("ACC_001", "CUST_88", 100.0)

    # Print Log Audit
    central_bank.print_transactions()