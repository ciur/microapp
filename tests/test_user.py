from fastapi.testclient import TestClient
from microapp.db.api import create_user


def test_user(db_session, app_test_client: TestClient):

    user = create_user(db_session, username="john2", email="john2@mail.com")
    data = {"username": "lili", "email": "popo"}
    response = app_test_client.post("/users", json=data)

    assert response.status_code == 200
    assert user
