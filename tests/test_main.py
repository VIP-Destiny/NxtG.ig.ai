"""Test main application."""

from fastapi.testclient import TestClient

from nextgigai.main import app

client = TestClient(app)

def test_read_main():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "NextGigAI"

def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
