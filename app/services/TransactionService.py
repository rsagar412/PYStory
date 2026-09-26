from app.models.Transaction import (Transaction, TransactionProcessingResult, TransactionStatus)
from app.validators.TransactionValidator import TransactionValidator
from decimal import Decimal
MAX_TRANSACTION_AMOUNT = Decimal("100000")

class TransactionService: 

    def __init__(self, validator: TransactionValidator):
        self.validator = validator

    def processTransaction(self, transaction: Transaction) -> TransactionProcessingResult:
        self.validator.validate(transaction)
        if transaction.amount > MAX_TRANSACTION_AMOUNT:
            return TransactionProcessingResult.REQUIRES_REVIEW
        if transaction.status.value == "SUCCESS":
            return TransactionProcessingResult.PROCESSED
        if transaction.status.value == "PENDING":
            return TransactionProcessingResult.PENDING
        return TransactionProcessingResult.REJECTED