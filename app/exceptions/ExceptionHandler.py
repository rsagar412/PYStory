from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.TransactionExceptions import (TransactionValidationException)


async def transaction_validation_exception_handler(
        request: Request,
        exc: TransactionValidationException
) -> JSONResponse:

    return JSONResponse(status_code=400, content={
        "errorCode": "TXN_VALIDATION_ERROR",
        "message": str(exc)
    })