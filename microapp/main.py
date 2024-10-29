from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from microapp.db import api as dbapi
from microapp.db.session import get_session
from microapp.models import User, NewUser

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user_endpoint(
    user: NewUser,
    db_session: Session = Depends(get_session),
) -> User:
    created_user = dbapi.create_user(
        db_session, username=user.username, email=user.email
    )

    return created_user
