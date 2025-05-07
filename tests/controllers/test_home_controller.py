# File: tests/controllers/test_home_controller.py

from fastapi.testclient import TestClient

BASE_ROUTE = "/api/"

def test_welcome_message(routes_client: TestClient) -> None:
    response = routes_client.get(BASE_ROUTE)

    assert response.status_code == 200

    json = response.json()
    assert "message" in json
    assert json["message"] == "Welcome to the GAP Python AI Workshop API!"

