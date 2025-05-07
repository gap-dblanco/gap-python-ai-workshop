# File: tests/controllers/test_healthcheck_controller.py
from unittest.mock import patch

from fastapi.testclient import TestClient

BASE_ROUTE = "/api/health"

def test_healthy(routes_client: TestClient) -> None:
    response = routes_client.get(BASE_ROUTE)
    assert response.status_code == 200


def test_sick(routes_client: TestClient) -> None:
    # Assuming your health endpoint checks database connectivity
    with patch(
        'src.controllers.healthcheck_controller.HealthcheckController._check_db_connection',
        return_value=False
    ):
        response = routes_client.get(BASE_ROUTE)
        assert response.status_code == 503  # Service Unavailable
        assert "sick" in response.json()["status"].lower()

