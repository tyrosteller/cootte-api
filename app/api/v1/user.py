from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas import user as userSchemas
from app.services.user import UserServices

dbSession = Depends(deps.get_db_session)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=userSchemas.UserResponse)
def sign_up(
    user_data: userSchemas.UserCreate, dbSession: Session = dbSession
) -> userSchemas.UserResponse:
    userServices = UserServices(dbSession)
    try:
        if userServices.is_user_exists(user_data):
            raise HTTPException(status_code=400, detail="Email already registered")

        new_user = userServices.create_user(user_data)
        dbSession.commit()
        return new_user

    except SQLAlchemyError as e:
        dbSession.rollback()
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}") from e
