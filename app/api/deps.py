from typing import Iterator

from database.session import SessionLocal
from sqlalchemy.orm import Session


def get_db_session() -> Iterator[Session]:
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
