from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# from sqlalchemy.orm import scoped_session

# SQLAlchemy 엔진 생성
engine = create_engine(settings.DATABASE_URL, echo=True)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 스코프 세션 생성 - 멀티스레딩에서 사용
# Session = scoped_session(SessionLocal)
