from decimal import Decimal
from pydantic import BaseModel, Field
from app.models.Transaction import *

class TransactionRequest(BaseModel):
    transaction_id : str = Field(min_length=5)
    merchant_id : str
    customer_id : str
    amount: Decimal
    currency: Currency
    status: TransactionStatus

class TransactionResponse(BaseModel):
    transaction_id : str
    status: TransactionStatus
    result: TransactionProcessingResult
