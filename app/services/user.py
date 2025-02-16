import bcrypt
from sqlalchemy.orm import Session

from app.models import user as userModels
from app.schemas import user as userSchemas


class UserServices:
    def __init__(self, dbSession: Session):
        self.dbSession = dbSession  # 세션을 클래스 초기화 시 주입

    def is_user_exists(self, user_data: userSchemas.UserCreate) -> bool:
        existing_user = (
            self.dbSession.query(userModels.UserAccount)
            .filter(
                userModels.UserAccount.email == user_data.email,
                userModels.UserAccount.login_type == user_data.login_type,
            )
            .first()
        )

        return existing_user is not None

    def create_user(self, user_data: userSchemas.UserCreate) -> userSchemas.UserResponse:
        hashed_password = bcrypt.hashpw(
            user_data.password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        new_user = userModels.UserAccount(
            email=user_data.email,
            login_type=1,
            status=-2,
            profile=userModels.UserProfile(nickname=user_data.nickname),
            password=userModels.UserPassword(password_hash=hashed_password),
        )

        self.dbSession.add(new_user)
        self.dbSession.flush()
        self.dbSession.refresh(new_user)

        return userSchemas.UserResponse.model_validate(new_user)


# def createUser(db_session: Session, user_data: userSchemas.UserCreate) -> userModels.User:
#     # 비즈니스 로직: 예를 들어, 사용자 이메일 중복 검사
#     # existingUser = (
#     #     db_session.query(userModels.User).filter(userModels.User.email == user_data.email).first()
#     # )
#     # if existingUser:
#     #     raise ValueError("Email already registered")

#     # 비즈니스 로직: 새로운 사용자 생성

#     new_user = userModels.UserAccount(
#         email=user_data.email, password=userModels.UserPassword(password_hash=user_data.password)
#     )

#     db_session.add(new_user)
#     db_session.commit()
#     db_session.refresh(new_user)

#     return new_user
