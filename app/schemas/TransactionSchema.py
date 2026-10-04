from decimal import Decimal
from pydantic import BaseModel, Field
from app.models.Transaction import *

class TransactionRequest(BaseModel):
    transaction_id : str = Field(min_length=5, max_length=50)
    merchant_id : str = Field(min_length=5, max_length=50)
    customer_id : str = Field(min_length=5, max_length=50)
    amount: Decimal = Field(gt=0)
    currency: Currency
    status: TransactionStatus

class TransactionResponse(BaseModel):
    transaction_id : str
    status: TransactionStatus
    result: TransactionProcessingResult
