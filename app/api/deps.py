from typing import Iterator

from sqlalchemy.orm import Session

from app.database.session import SessionLocal


def get_db_session() -> Iterator[Session]:
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
