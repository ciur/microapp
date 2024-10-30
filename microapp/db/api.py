import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from microapp.db.orm import Group, User
from microapp import models
from typing import Tuple


def create_user(
    session: Session, username: str, email: str
) -> Tuple[models.User | None, models.Error | None]:
    error = None

    user = User(id=uuid.uuid4(), username=username, email=email)
    session.add(user)

    try:
        session.commit()
    except IntegrityError as e:
        stre = str(e)
        # postgres unique integrity error
        if "unique" in stre and "username" in stre:
            attr_err = models.AttrError(
                name="username", message="Username must be unique"
            )
            error = models.Error(attrs=[attr_err])
        # sqlite unique integrity error
        if "UNIQUE" in stre and ".username" in stre:
            attr_err = models.AttrError(
                name="username", message="Username must be unique"
            )
            error = models.Error(attrs=[attr_err])

    return models.User.model_validate(user), error


def create_group(
    session: Session, name: str
) -> Tuple[models.Group | None, models.Error | None]:
    error = None

    group = Group(name=name)
    session.add(group)

    try:
        session.commit()
    except IntegrityError as e:
        stre = str(e)
        # postgres unique integrity error
        if "unique" in stre and "name" in stre:
            attr_err = models.AttrError(name="name", message="Name must be unique")
            error = models.Error(attrs=[attr_err])
        # sqlite unique integrity error
        if "UNIQUE" in stre and ".name" in stre:
            attr_err = models.AttrError(name="name", message="Name must be unique")
            error = models.Error(attrs=[attr_err])

    if error:
        return None, error

    return models.Group.model_validate(group), None
