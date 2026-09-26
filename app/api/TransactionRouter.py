from fastapi import APIRouter
from app.schemas.TransactionSchema import (TransactionRequest, TransactionResponse)
from app.models.Transaction import Transaction
from app.services.TransactionService import TransactionService
from app.validators.TransactionValidator import TransactionValidator

router = APIRouter(
    prefix = "/api/v1/transaction",
    tags=["Transactions"],
)

validator = TransactionValidator()
transaction_service = TransactionService(validator)

@router.post("/", response_model=TransactionResponse)
def create_transaction(request: TransactionRequest): 
    transaction = Transaction (
    transaction_id = request.transaction_id,
    merchant_id = request.merchant_id,
    customer_id = request.customer_id,
    amount = request.amount,
    currency= request.currency,
    status=request.status
    )
    result = transaction_service.processTransaction(transaction)
    return TransactionResponse(transaction_id=transaction.transaction_id,
                               status = transaction.status.value,
                               result=result)

@router.get("/health")
def transaction_health():
    return {"service": "transaction", "status": "UP"}

