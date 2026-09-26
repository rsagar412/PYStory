from app.models.Transaction import Transaction
from app.validators.TransactionValidator import TransactionValidator
from decimal import Decimal
MAX_TRANSACTION_AMOUNT = Decimal("100000")

class TransactionService: 

    def __init__(self, validator: TransactionValidator):
        self.validator = validator

    def processTransaction(self, transaction: Transaction) -> str:
        self.validator.validate(transaction)
        if transaction.amount > MAX_TRANSACTION_AMOUNT:
            return "REQUIRES_REVIEW"
        if transaction.status.value == "SUCCESS":
            return "PROCESSED"
        if transaction.status.value == "PENDING":
            return "PENDING"
        return "REJECTED"