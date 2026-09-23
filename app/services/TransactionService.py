from app.models.Transaction import Transaction
from app.validators.TransactionValidator import TransactionValidator

class TransactionService: 

    def __init__(self, validator: TransactionValidator):
        self.validator = validator

    def processTransaction(self, transaction: Transaction) -> str:
        self.validator.validate(transaction)
        if transaction.status.value == "SUCCESS":
            return "PROCESSED"
        if transaction.status.value == "PENDING":
            return "PENDING"
        return "REJECTED"