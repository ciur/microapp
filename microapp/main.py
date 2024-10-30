from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from microapp.db.con import Session
from microapp.db import api as dbapi
from microapp.models import NewGroup, Group, User

router = APIRouter(prefix="/groups")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    with Session() as db_session:
        user = db_session.get(dbapi.User, token)

    return user


@router.post("/")
def create_group_endpoint(
    group: NewGroup, current_user: User = Depends(get_current_user)
) -> Group:
    with Session.begin() as db_session:
        created_group, error = dbapi.create_group(db_session, name=group.name)

    if error:
        raise HTTPException(status_code=400, detail=error.model_dump())

    return created_group
