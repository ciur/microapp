from fastapi.testclient import TestClient
from microapp.db.api import create_user
from microapp import models


def test_user(db_session, app_test_client: TestClient):

    user = create_user(db_session, username="john2", email="john2@mail.com")
    data = {"username": "lili", "email": "popo"}
    response = app_test_client.post("/users", json=data)

    assert response.status_code == 200
    assert user


def test_user_again(db_session, app_test_client: TestClient):

    user = create_user(db_session, username="john2", email="john2@mail.com")
    data = {"username": "lili", "email": "popo"}
    response = app_test_client.post("/users", json=data)

    assert response.status_code == 200
    assert user


def test_username_is_unique(db_session, app_test_client: TestClient):
    data = {"username": "lili", "email": "popo"}
    response = app_test_client.post("/users", json=data)
    assert response.status_code == 200

    data = {"username": "lili", "email": "popo"}
    response = app_test_client.post("/users", json=data)
    assert response.status_code == 400

    json_response = response.json()
    error = models.Error(**json_response["detail"])

    assert error.attrs[0].name == "username"
    assert error.attrs[0].message == "Username must be unique"
