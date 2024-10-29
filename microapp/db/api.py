import uuid
from microapp.db.orm import User
from microapp import models


def create_user(session, username: str, email: str) -> models.User:
    user = User(id=uuid.uuid4(), username=username, email=email)
    session.add(user)
    session.commit()

    return models.User.model_validate(user)
