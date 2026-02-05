"""Basic tests for the API."""
import pytest
from fastapi.testclient import TestClient
from design_system_agent.api.main import app

client = TestClient(app)


def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()


def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_api_docs():
    """Test that API docs are accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
