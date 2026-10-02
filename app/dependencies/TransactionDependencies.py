from app.services.TransactionService import TransactionService
from app.validators.TransactionValidator import TransactionValidator
from app.repositories.TransactionRepository import TransactionRepository

def get_transaction_service() -> TransactionService:
    validator = TransactionValidator()
    repository = TransactionRepository()
    return TransactionService(validator, repository)