import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


SQLALCHEMY_DATABASE_URL = os.environ.get("PAPERMERGE__DATABASE__URL")

if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("PAPERMERGE__DATABASE__URL env var is empty")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=NullPool,
)

Session = sessionmaker(engine)
