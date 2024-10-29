import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from microapp.db.base import Base
from microapp.db.con import engine, Session
from microapp.main import router


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(engine)

    with Session.begin() as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture()
def app_test_client():
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)
