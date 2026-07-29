from fastapi.testclient import TestClient

from src.fastapi_demo.cors_post import app

client = TestClient(app)


def test_cors_header() -> None:
    resp = client.get("/cors", headers={"Origin": "http://example.com"})
    assert resp.status_code == 200
    assert resp.headers.get("access-control-allow-origin") == "http://example.com"
    assert resp.headers.get("access-control-allow-credentials") == "true"


def test_cors_without_origin() -> None:
    resp = client.get("/cors")
    assert resp.status_code == 200


def test_batch_empty() -> None:
    resp = client.post("/weather/batch", json={"cities": []})
    assert resp.status_code == 200
    assert resp.json() == []


def test_batch_wrong_key() -> None:
    resp = client.post("/weather/batch", json={"xxx": []})
    assert resp.status_code == 422
