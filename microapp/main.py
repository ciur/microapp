from fastapi import APIRouter

from microapp.db.engine import Session
from microapp.db import api as dbapi
from microapp.models import User, NewUser

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user_endpoint(user: NewUser) -> User:
    with Session.begin() as db_session:
        created_user = dbapi.create_user(
            db_session, username=user.username, email=user.email
        )

    return created_user
