import uuid
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from microapp.db.base import Base
from microapp.db import orm
from microapp.db.con import engine, Session
from microapp.main import router


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(engine)

    with Session() as session:
        yield session

    Base.metadata.drop_all(engine)


@pytest.fixture()
def app_test_client(user: orm.User):
    app = FastAPI()
    app.include_router(router)

    headers = {"Authorization": f"Bearer {user.id}"}
    return TestClient(app, headers=headers)


@pytest.fixture()
def user(make_user) -> orm.User:
    return make_user(username="random")


@pytest.fixture()
def make_user(db_session: Session):
    def _maker(username: str):
        user_id = uuid.uuid4()

        db_user = orm.User(
            id=user_id,
            username=username,
            email=f"{username}@mail.com",
        )
        db_session.add(db_user)
        db_session.commit()

        return db_user

    return _maker
