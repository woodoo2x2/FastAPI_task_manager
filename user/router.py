from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db_session
from user.logic import UserLogic
from user.schemas import UserLoginSchema, UserCreateSchema
from user.service import UserService

router = APIRouter(prefix="/user", tags=["user"])


def get_user_logic(db_session: Session = Depends(get_db_session)) -> UserLogic:
    return UserLogic(db_session=db_session)


def get_user_service(user_logic: UserLogic = Depends(get_user_logic)) -> UserService:
    return UserService(user_logic=user_logic)


@router.post("/login", response_model=UserLoginSchema)
async def login(body: UserCreateSchema, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(body.username, body.password)
