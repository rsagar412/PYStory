from app.models.Transaction import Transaction
from app.exceptions.TransactionExceptions import TransactionValidationException

class TransactionValidator:

    def validate(self, transaction: Transaction) -> None:
        if not transaction.transaction_id:
            raise TransactionValidationException("Transaction Id is required")

        if not transaction.merchant_id: 
            raise TransactionValidationException("Merchant Id is required") 

        if not transaction.customer_id: 
            raise TransactionValidationException("Customer Id is required") 

        if transaction.amount <= 0: 
            raise TransactionValidationException("Transaction amount must be greater than zero.")   
        
        if transaction.transaction_id.__len__ < 5:
          raise TransactionValidationException("Transaction Id must be 5 characters long.")