from fastapi import FastAPI

from app.api.v1 import user
from app.core.config import settings

app = FastAPI()

# v1 버전의 API를 등록
app.include_router(user.router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"profile": settings.PROFILE}
