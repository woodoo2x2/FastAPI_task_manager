from fastapi import APIRouter, Depends

from user.dependency import get_user_service
from user.schemas import UserLoginSchema, UserCreateSchema
from user.service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login", response_model=UserLoginSchema)
async def login(body: UserCreateSchema, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(body.username, body.password)
