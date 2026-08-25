from unittest.mock import patch

from fastapi.testclient import TestClient

from src.fastapi_demo.cors_post import app
from src.main import app as main_app

client = TestClient(app)
main_client = TestClient(main_app)


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


@patch("src.main.rag_answer", return_value="mock answer")
def test_qa_get_returns_200(mock_rag: object) -> None:
    resp = main_client.get("/qa", params={"question": "test"})
    assert resp.status_code == 200
    assert resp.json() == {"answer": "mock answer"}
