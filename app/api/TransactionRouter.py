from fastapi import APIRouter

router = APIRouter(
    prefix = "/api/v1/transaction",
    tags=["Transactions"],
)

@router.get("/health")
def transaction_health():
    return {"service": "transaction", "status": "UP"}