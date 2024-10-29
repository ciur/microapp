import os
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


def get_engine():
    SQLALCHEMY_DATABASE_URL = os.environ.get("PAPERMERGE__DATABASE__URL")

    if SQLALCHEMY_DATABASE_URL is None:
        raise ValueError("PAPERMERGE__DATABASE__URL env var is empty")

    return create_engine(
        SQLALCHEMY_DATABASE_URL,
        poolclass=NullPool,
    )
