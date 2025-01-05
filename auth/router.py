from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from auth.service import AuthService
from user.logic import UserLogic
from exceptions import UserNotFoundException, UserNotCorrectPasswordException
from user.router import get_user_logic
from user.schemas import UserLoginSchema, UserCreateSchema

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service(user_logic: UserLogic = Depends(get_user_logic)) -> AuthService:
    return AuthService(user_logic)



@router.post("/login", response_model=UserLoginSchema)
async def login(body: UserCreateSchema,
                auth_service: AuthService = Depends(get_auth_service)):
    try:
        data = auth_service.login(body.username, body.password)
        return data
    except UserNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
    except UserNotCorrectPasswordException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

