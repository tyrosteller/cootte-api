import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# 기본적으로 사용할 .env 파일을 지정
ENV_FILE = os.getenv("ENV_FILE", ".env.development")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8")

    PROFILE: str = Field(default="noenv")
    DATABASE_URL: str = Field(default="noenv")


# Settings 인스턴스를 전역적으로 사용 가능하게 설정
settings = Settings()
