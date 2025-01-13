from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from auth.service import AuthService
from exceptions import UserNotFoundException, UserNotCorrectPasswordException
from user.dependency import get_auth_service
from user.schemas import UserLoginSchema, UserCreateSchema
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/auth", tags=["auth"])


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


@router.get("/login/google",
            response_class=RedirectResponse)
async def google_login(auth_service: AuthService = Depends(get_auth_service)):
    url = auth_service.get_google_redirect_url()
    print(url)
    return RedirectResponse(url)

@router.get("/google")
async def google_login(code: str,
                       auth_service: AuthService = Depends(get_auth_service),
                       ):
    return auth_service.google_auth(code)