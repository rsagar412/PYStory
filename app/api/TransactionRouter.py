from fastapi import APIRouter, Depends, status
from app.services.TransactionService import TransactionService
from app.dependencies.TransactionDependencies import get_transaction_service
from app.schemas.TransactionSchema import (TransactionRequest, TransactionResponse)
from app.models.Transaction import Transaction


router = APIRouter(
    prefix = "/api/v1/transaction",
    tags=["Transactions"],
)

@router.post("/create", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(request: TransactionRequest, transaction_service: TransactionService = Depends(get_transaction_service)): 
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
                               status = transaction.status,
                               result=result)

@router.get("/health")
def transaction_health():
    return {"service": "transaction", "status": "UP"}

