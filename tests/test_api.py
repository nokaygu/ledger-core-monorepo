from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

def test_read_ledger():
    response = client.get("/ledger/owner1")
    assert response.status_code == 200
    assert "balance" in response.json()

def test_create_ledger_entry():
    unique_nonce = str(uuid.uuid4())
    response = client.post("/ledger", json={
        "owner_id": "owner1",
        "operation": "DAILY_REWARD",
        "amount": 1,
        "nonce": unique_nonce
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Transaction successful"