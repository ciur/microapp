# FastAPI + PyTest + SqlAlchemy + Postgresql/Sqlite

Minimal stucture of FastAPI app with pytest which features
SqlAlchemy over Postgresql.

This small project illustrates how to use FastAPI + PyTest + SqlAlchemy + 
Postgresql (and sqlite) + pydantic in one project.

The point is to make pytest succeed regardless if database is Postgres or sqlite.

PostgreSql is trickier to deal with because of: 
https://docs.sqlalchemy.org/en/20/faq/metadata_schema.html#my-program-is-hanging-when-i-say-table-drop-metadata-drop-all


## Run test with Postgres

$ export PAPERMERGE__DATABASE__URL="postgresql://user:pass@localhost:5432
/test_microapp_db"
$ poetry run pytest


# Run test with Sqlite

$ export PAPERMERGE__DATABASE__URL="sqlite:///test.sqlite3"
$ poetry run pytest
