from app.validators import validate_transaction

def process_transaction(transaction: dict) -> str:
    if not validate_transaction(transaction): 
        return "INVALID"
        
    if transaction["status"] == "SUCCESS": 
        return "PROCESSED"
        
    if transaction["status"] == "PENDING":
        return "PENDING"
        
    return "REJECTED"    