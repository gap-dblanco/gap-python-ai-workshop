# File: tests/controllers/test_user_controller.py
from fastapi.testclient import TestClient

BASE_ROUTE = "/api/users"

def test_status(routes_client: TestClient) -> None:
    response = routes_client.get(BASE_ROUTE)
    assert response.status_code == 200


