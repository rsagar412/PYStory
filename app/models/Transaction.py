from decimal import Decimal    #production grade application needs decimal for exact values instead of fload since there can be n number of values after decimal
from dataclasses import dataclass   #automatically generates the constructor to help initialize the values similar to lombok
from enum import Enum

class Currency(str, Enum)
    INR = "INR"
    USD = "USD"
    EUR = "EUR"

@dataclass       
class Transaction: 
    transaction_id: str
    merchant_id: str
    amount: float
    currency: str
    status: str
    ):



"""
transaction = Transaction(
    transaction_id="TXN10001",
    merchant_id="MERCHANT001",
    amount=Decimal("1500.50"),
    currency="INR",
    status="SUCCESS"
)
"""