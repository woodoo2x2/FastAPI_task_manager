from fastapi import APIRouter, Depends

from app.dependency import get_user_service
from app.users.schemas import UserLoginSchema, UserCreateSchema
from app.users.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/login", response_model=UserLoginSchema)
async def login(
    body: UserCreateSchema, user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(body)
