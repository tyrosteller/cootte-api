from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class UserAccount(Base):
    __tablename__ = "accounts"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    login_type = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, default=-2)
    created_at = Column(DateTime, default=func.now())

    profile = relationship("UserProfile", back_populates="account", uselist=False)
    password = relationship("UserPassword", back_populates="account", uselist=False)


class UserProfile(Base):
    __tablename__ = "profiles"
    __table_args__ = {"schema": "user"}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("user.accounts.id", name="fk_user_profiles_user_accounts"),
        nullable=False,
    )
    nickname = Column(String, unique=True, nullable=False)
    image_url = Column(String, nullable=True)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    account = relationship("UserAccount", back_populates="profile")


class UserPassword(Base):
    __tablename__ = "user_passwords"
    __table_args__ = {"schema": "auth"}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("user.accounts.id", name="fk_user_profiles_user_accounts"),
        nullable=False,
    )
    password_hash = Column(String(60), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    account = relationship("UserAccount", back_populates="password")
