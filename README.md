# FastAPI + PyTest + SqlAlchemy + Postgresql/Sqlite

Minimal stucture of FastAPI app with pytest which features
SqlAlchemy over Postgresql.

This small project illustrates how to use FastAPI + PyTest + SqlAlchemy + 
Postgresql (and sqlite) + pydantic in one project.

The point is to make pytest succeed regardless if database is Postgres or sqlite.

PostgreSql is trickier to deal with because of: 
https://docs.sqlalchemy.org/en/20/faq/metadata_schema.html#my-program-is-hanging-when-i-say-table-drop-metadata-drop-all


