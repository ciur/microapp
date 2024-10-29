import uuid
from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from microapp.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, insert_default=uuid.uuid4())
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
