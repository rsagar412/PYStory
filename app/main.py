from decimal import Decimal
from app.models.Transaction import(Currency, Transaction, TransactionStatus)
from app.exceptions.TransactionExceptions import TransactionValidationException
from app.validators.TransactionValidator import TransactionValidator

def main() -> None:
    transaction = Transaction(
        transaction_id = "TXN11",
        merchant_id = "MRCH101",
        customer_id = "101",
        amount=Decimal("1500.50"),
        currency=Currency.INR,
        status=TransactionStatus.SUCCESS
    )

    

    validator = TransactionValidator()

    try: 
        validator.validate(transaction)
        print("Transaction Validation successful")

    except TransactionValidationException as error:
        print(f"Transaction validation failed: {error}")

    print(f"Txn Id: {transaction.transaction_id}")
    print(f"Merchant Id: {transaction.merchant_id}")
    print(f"Amount: {transaction.amount}")
    print(f"Currency: {transaction.currency}")
    print(f"Status: {transaction.status.value}")

    print("Thank you for banking with us.")

if __name__ == "__main__":
    main()