import os
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


@lru_cache()
def get_engine():
    SQLALCHEMY_DATABASE_URL = os.environ.get('PAPERMERGE__DATABASE__URL')

    return create_engine(
        SQLALCHEMY_DATABASE_URL,
        poolclass=NullPool,
    )
