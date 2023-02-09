from fastapi import FastAPI
from fastapi.testclient import TestClient

from pingpong.main import create_app


def test_create_app_and_do_ping():
    app = create_app()

    assert isinstance(app, FastAPI)

    with TestClient(app) as client:
        response = client.get("/ping")

        assert response.status_code == 200
        assert response.json()["message"] == "pong"
