from decimal import Decimal
from unittest.mock import Mock
from app.models.Transaction import (
    Transaction, TransactionStatus, TransactionProcessingResult,
)
from app.services.TransactionService import TransactionService
from app.validators.TransactionValidator import TransactionValidator

def create_service():
    validator = Mock(spec = TransactionValidator)
    repository = Mock()
    return TransactionService(
        validator=validator,
        repository=repository
    ), validator, repository

def test_successful_transaction():
    service, validator, repository = create_service()
    transaction = Transaction(
        transaction_id="TXN10001",
        merchant_id="MERCHANT001",
        customer_id="CUSTOMER001",
        amount=Decimal("1500.50"),
        currency="INR",
        status=TransactionStatus.SUCCESS
    )
    result = service.processTransaction(transaction)
    assert result == TransactionProcessingResult.PROCESSED
    assert transaction.processing_result == (TransactionProcessingResult.PROCESSED)
    repository.save.assert_called_once_with(transaction)

def test_high_value_transaction_requires_review():

    service, validator, repository = create_service()

    transaction = Transaction(
        transaction_id="TXN10002",
        merchant_id="MERCHANT001",
        customer_id="CUSTOMER001",
        amount=Decimal("150001"),
        currency="INR",
        status=TransactionStatus.SUCCESS
    )

    result = service.processTransaction(transaction)

    assert result == TransactionProcessingResult.REQUIRES_REVIEW

    assert transaction.processing_result == (
        TransactionProcessingResult.REQUIRES_REVIEW
    )

    repository.save.assert_called_once_with(transaction)

def test_pending_transaction():
    service, validator, repository = create_service()
    transaction = Transaction(
            transaction_id="TXN10002",
            merchant_id="MERCHANT001",
            customer_id="CUSTOMER001",
            amount=Decimal("150000"),
            currency="INR",
            status=TransactionStatus.SUCCESS
        )

    result = service.processTransaction(transaction)
    assert result == TransactionProcessingResult.PENDING
    repository.save.assert_called_once_with(transaction)


def test_transaction_is_validated_before_processing():

    service, validator, repository = create_service()
    transaction = Transaction(
        transaction_id="TXN10005",
        merchant_id="MERCHANT001",
        customer_id="CUSTOMER001",
        amount=Decimal("5000"),
        currency="INR",
        status=TransactionStatus.SUCCESS
    )

    service.processTransaction(transaction)

    validator.validate.assert_called_once_with(transaction)    