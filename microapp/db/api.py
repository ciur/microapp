from microapp.db.orm import User
from microapp import models


def create_user(session, username: str, email: str) -> models.User:
    user = User(username=username, email=email)
    session.add(user)
    session.commit()

    return models.User.model_validate(user)
