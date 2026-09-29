import pytest

from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():

    return TestClient(app)



@pytest.fixture
def auth_headers(client):

    response = client.post(
        "/auth/login",
        json={
            "email": "vardhan@gmail.com",
            "password": "admin123"
        }
    )


    token = response.json()["data"]["access_token"]


    return {
        "Authorization": f"Bearer {token}"
    }