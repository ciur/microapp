import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from microapp.db.base import Base
from microapp.db.engine import get_engine
from microapp.main import router


@pytest.fixture(scope="function")
def db_session():
    engine = get_engine()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture()
def app_test_client():
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)
