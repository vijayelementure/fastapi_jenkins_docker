from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_register_device():
    response = client.post("/device/register-device", json={"device_id": "123"}) # noqa
    assert response.status_code == 200


def test_status():
    response = client.get("/device/status/123")
    assert response.status_code == 200
