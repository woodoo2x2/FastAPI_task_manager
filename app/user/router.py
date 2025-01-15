from fastapi import APIRouter, Depends

from app.user.dependency import get_user_service
from app.user.schemas import UserLoginSchema, UserCreateSchema
from app.user.service import UserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login", response_model=UserLoginSchema)
async def login(body: UserCreateSchema, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(body.username, body.password)
