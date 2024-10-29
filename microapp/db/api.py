import uuid
from sqlalchemy.orm import Session
from microapp.db.orm import User
from microapp import models


def create_user(session: Session, username: str, email: str) -> models.User:
    user = User(id=uuid.uuid4(), username=username, email=email)
    session.add(user)
    validated_user = models.User.model_validate(user)
    session.commit()

    return validated_user
