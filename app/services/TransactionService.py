from app.models.Transaction import (Transaction, TransactionProcessingResult, TransactionStatus)
from app.validators.TransactionValidator import TransactionValidator
from decimal import Decimal
from app.repositories.TransactionRepository import TransactionRepository
MAX_TRANSACTION_AMOUNT = Decimal("100000")

class TransactionService: 

    def __init__(self, validator: TransactionValidator, repository: TransactionRepository):
        self.validator = validator
        self.repository = repository

    def processTransaction(self, transaction: Transaction) -> TransactionProcessingResult:
        self.validator.validate(transaction)
        if transaction.amount > MAX_TRANSACTION_AMOUNT:
            result = TransactionProcessingResult.REQUIRES_REVIEW
        elif transaction.status.value == "SUCCESS":
            result = TransactionProcessingResult.PROCESSED
        elif transaction.status.value == "PENDING":
            result = TransactionProcessingResult.PENDING
        else:
            result = TransactionProcessingResult.REJECTED
        transaction.processing_result = result
        self.repository.save(transaction)
        return result

    def get_transaction(self, transaction_id: str,) -> Transaction | None: 
        return self.repository.find_by_id(transaction_id)