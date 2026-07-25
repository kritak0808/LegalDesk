"""
LegalDesk AI v1.0.0-RC1 Comprehensive API Route Test Suite
Validates status codes and responses for all FastAPI v1 routers.
"""
import sys
from fastapi.testclient import TestClient
sys.path.insert(0, '.')

from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "1.0.0-RC1"
    assert data["status"] == "Operational"

def test_health_endpoints():
    r1 = client.get("/api/v1/health")
    assert r1.status_code == 200
    assert r1.json()["status"] == "healthy"

    r2 = client.get("/api/v1/health/liveness")
    assert r2.status_code == 200
    assert r2.json()["status"] == "alive"

def test_system_info_endpoint():
    r = client.get("/api/v1/system/info")
    assert r.status_code == 200
    assert r.json()["version"] == "1.0.0-RC1"
