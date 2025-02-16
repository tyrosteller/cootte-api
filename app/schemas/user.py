from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BaseUserAccount(BaseModel):
    id: int
    email: str
    login_type: int
    status: int
    created_at: datetime

    class Config:
        from_attributes = True


class BaseUserProfile(BaseModel):
    nickname: str
    image_url: Optional[str] = None
    updated_at: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password: str = Field(..., min_length=8)  # 비밀번호 최소 8자 이상
    nickname: str = Field(..., min_length=3, max_length=50)
    login_type: int


class UserResponse(BaseModel):
    id: int
    email: str
    status: int
    login_type: int
    created_at: datetime
    profile: BaseUserProfile

    class Config:
        from_attributes = True
