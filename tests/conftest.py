import pytest

from app.repositories.TransactionRepository import TransactionRepository
from app.validators.TransactionValidator import TransactionValidator
from app.services.TransactionService import TransactionService
from app.dependencies.TransactionDependencies import get_transaction_service
from app.main import app

@pytest.fixture
def transaction_repository():
    return TransactionRepository()


@pytest.fixture
def transaction_validator():
    return TransactionValidator()

@pytest.fixture
def transaction_service(transaction_repository, transaction_validator):
    return TransactionService(
        validator = transaction_validator,
        repository=transaction_repository
    )

@pytest.fixture
def override_transaction_service(transaction_service):
    def override():
        return transaction_service
    app.dependency_overrides[
        get_transaction_service
    ] = override

    yield transaction_service
    app.dependency_overrides.clear()