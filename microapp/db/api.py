import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from microapp.db.orm import User
from microapp import models
from typing import Tuple


def create_user(
    session: Session, username: str, email: str
) -> Tuple[models.User, models.Error | None]:
    error = None

    user = User(id=uuid.uuid4(), username=username, email=email)
    session.add(user)
    validated_user = models.User.model_validate(user)

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

    return validated_user, error
