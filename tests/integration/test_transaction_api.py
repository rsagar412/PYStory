from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_create_successful_transaction():
   response = client.post(
      "/api/v1/transaction/create",
      json = {"transaction_id": "TXN10001",
            "merchant_id": "MERCHANT001",
            "customer_id": "CUSTOMER001",
            "amount": "1500.50",
            "currency": "INR",
            "status": "SUCCESS",}
   )

   assert response.status_code == 201
   body =response.json()

   assert body["transaction_id"] == "TXN10001"
   assert body["status"] == "SUCCESS"
   assert body["result"] == "PROCESSED"



def test_create_transaction_with_invalid_amount():
    response = client.post(
        "/api/v1/transaction/create",
        json={
            "transaction_id": "TXN10002",
            "merchant_id": "MERCHANT001",
            "customer_id": "CUSTOMER001",
            "amount": "-100",
            "currency": "INR",
            "status": "SUCCESS",
        },
    )

    assert response.status_code == 400

    body = response.json()

    assert body["errorCode"] == "TXN_VALIDATION_ERROR"
    assert body["message"] == (
        "Transaction amount must be greater than zero."
    )

def test_create_transaction_with_invalid_transaction_id():

    response = client.post(
        "/api/v1/transaction/create",
        json={
            "transaction_id": "TXN",
            "merchant_id": "MERCHANT001",
            "customer_id": "CUSTOMER001",
            "amount": "1500.50",
            "currency": "INR",
            "status": "SUCCESS",
        },
    )

    assert response.status_code == 422


def test_create_transaction_with_invalid_transaction_id():

    response = client.post(
        "/api/v1/transaction/create",
        json={
            "transaction_id": "TXN",
            "merchant_id": "MERCHANT001",
            "customer_id": "CUSTOMER001",
            "amount": "1500.50",
            "currency": "INR",
            "status": "SUCCESS",
        },
    )

    assert response.status_code == 422


def test_create_pending_transaction():
    response = client.post(
        "/api/v1/transaction/create",
    json = {
            "transaction_id": "TXN10004",
            "merchant_id": "MERCHANT001",
            "customer_id": "CUSTOMER001",
            "amount": "1500.50",
            "currency": "INR",
            "status": "PENDING",
    })

    assert response.status_code == 201
    body = response.json()
    assert body["result"] == "PENDING"

def test_get_transaction(override_transaction_service):

    client.post("/api/v1/transaction/create",
        json={
            "transaction_id": "TXN20001",
            "merchant_id": "MERCHANT001",
            "customer_id": "CUSTOMER001",
            "amount": "1500.50",
            "currency": "INR",
            "status": "SUCCESS",
        },
    )
    response = client.get("/api/v1/transaction/TXN20001")
    assert response.status_code == 200
    body = response.json()
    assert body["transaction_id"] == "TXN20001"
    assert body["status"] == "SUCCESS"
    assert body["result"] == "PROCESSED"
