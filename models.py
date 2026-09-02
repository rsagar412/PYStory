from typing import TypedDict

#describing the structure of the transaction
class Transaction (TypedDict):
    transaction_id: str
    merchant_id: str
    amount: float
    currency: str
    status: str