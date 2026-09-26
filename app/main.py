from fastapi import FastAPI
from app.api.TransactionRouter import router as transaction_router
from app.exceptions.ExceptionHandler import (transaction_validation_exception_handler)
from app.exceptions.TransactionExceptions import (TransactionValidationException)

app = FastAPI(
    title = "FinAI",
    description = "Intelligent Financial Transaction Platform",
    version="1.0.0",
)

app.add_exception_handler(TransactionValidationException, transaction_validation_exception_handler)
app.include_router(transaction_router)


@app.get("/")
def health_check():
    return {"status" : "UP"}

# Command Line code
# from decimal import Decimal
# from app.models.Transaction import(Currency, Transaction, TransactionStatus)
# from app.exceptions.TransactionExceptions import TransactionValidationException
# from app.validators.TransactionValidator import TransactionValidator

# def main() -> None:
#     transaction = Transaction(
#         transaction_id = "TXN11",
#         merchant_id = "MRCH101",
#         customer_id = "101",
#         amount=Decimal("1500.50"),
#         currency=Currency.INR,
#         status=TransactionStatus.SUCCESS
#     )

    

#     validator = TransactionValidator()

#     try: 
#         validator.validate(transaction)
#         print("Transaction Validation successful")

#     except TransactionValidationException as error:
#         print(f"Transaction validation failed: {error}")

#     print(f"Txn Id: {transaction.transaction_id}")
#     print(f"Merchant Id: {transaction.merchant_id}")
#     print(f"Amount: {transaction.amount}")
#     print(f"Currency: {transaction.currency}")
#     print(f"Status: {transaction.status.value}")

#     print("Thank you for banking with us.")

# if __name__ == "__main__":
#     main()