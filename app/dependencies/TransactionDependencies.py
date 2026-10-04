from app.services.TransactionService import TransactionService
from app.validators.TransactionValidator import TransactionValidator
from app.repositories.TransactionRepository import TransactionRepository

transaction_repository = TransactionRepository()
transaction_validator = TransactionValidator()

def get_transaction_service() -> TransactionService:

    return TransactionService(validator = transaction_validator, repository = transaction_repository)