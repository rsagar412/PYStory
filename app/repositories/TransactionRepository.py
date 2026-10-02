from app.models.Transaction import Transaction

class TransactionRepository:

    def __init__(self):
        self._transactions: dict[str, Transaction] = {}
    def save(self,transaction: Transaction) -> Transaction:
        self._transactions[transaction.transaction_id] = transaction
        return transaction

    def find_by_id(self, transaction_id: str) -> Transaction | None:
        return self._transactions.get(transaction_id)