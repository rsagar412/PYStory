from app.processors import process_transaction

def main() -> None:
    
   transaction = {
   "transaction_id": "txn1",
   "merchant_id": "mrchnt1",
   "amount": -500.5,
   "currency": "INR",
   "status": "SUCCESS"}
   
   result = process_transaction(transaction)
   
   print(f"Transaction result: {result}")
   
if __name__ == "__main__":
    main()
   
   