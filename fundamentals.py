merchant_id : str = "Merchant_id"
amount: float = 1000.0
flag: bool = True
print(merchant_id)

#lists are mutable ordered collection of items
merchants: list [str] = []
merchants.append("Amazon")
merchants.append("SBI")
merchants.append("PNB")

print(merchants)
print(merchants[1])
print(merchants[-1])

#tuples are immutable collection of items
transaction_status: tuple[str, str] = ("txn1","txn2")
print(transaction_status)

#sets , stores unique values 
currencies: set[str] = ("INR", "USD", "JPY")
print(currencies)
SUPPORTED_CURRENCIES = {"INR", "CPY"}
if currencies not in SUPPORTED_CURRENCIES:
        print(currencies)
        
#dictionaries, similar to java map<String, object>
transaction = {"transaction_id": "TXN001"}