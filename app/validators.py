SUPPORTED_CURRENCIES = {"INR", "USD", "EUR"}

SUPPORTED_STATUSES = {
  "SUCCESS", "FAILED", "PENDING"}


def validate_transaction(transaction: dict) -> bool:
    required_fields = {
    "transaction_id", 
    "merchant_id",
    "amount",
    "currency",
    "status"
    }     
    if not required_fields.issubset(transaction.keys()):
        return False
            
    if not transaction["transaction_id"]:
        return False
        
    if not transaction["merchant_id"]:
        return False
        
    if transaction["amount"] <= 0:
        return False
        
    if transaction["currency"] not in SUPPORTED_CURRENCIES:
        return False
        
    if transaction["status"] not in SUPPORTED_STATUSES:
        return False
        
    return True    