from fastapi import APIRouter, HTTPException
from microapp.db.con import Session
from microapp.db import api as dbapi
from microapp.models import User, NewUser

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user_endpoint(user: NewUser) -> User:
    with Session.begin() as db_session:
        created_user, error = dbapi.create_user(
            db_session, username=user.username, email=user.email
        )

    if error:
        raise HTTPException(status_code=400, detail=error.model_dump())

    return created_user
