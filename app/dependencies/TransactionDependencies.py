from app.services.TransactionService import TransactionService
from app.validators.TransactionValidator import TransactionValidator

def get_transaction_service() -> TransactionService:
    validator = TransactionValidator()
    return TransactionService(validator)