import uuid

from pydantic import BaseModel, ConfigDict


class NewUser(BaseModel):
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class User(NewUser):
    id: uuid.UUID


class AttrError(BaseModel):
    name: str
    message: str


class Error(BaseModel):
    attrs: list[AttrError] | None = None
    messages: list[str] | None = None
