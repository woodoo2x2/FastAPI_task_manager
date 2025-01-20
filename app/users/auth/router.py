from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from starlette import status

from app.users.auth.service import AuthService
from app.exceptions import UserNotFoundException, UserNotCorrectPasswordException
from app.dependency import get_auth_service
from app.users.schemas import UserLoginSchema, UserCreateSchema

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserLoginSchema)
async def login(body: UserCreateSchema,
                auth_service: AuthService = Depends(get_auth_service)):
    try:
        data = await auth_service.login(body.username, body.password)
        return data
    except UserNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
    except UserNotCorrectPasswordException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)


@router.get("/login/google",
            response_class=RedirectResponse)
async def google_login(auth_service: AuthService = Depends(get_auth_service)):
    url = auth_service.get_google_redirect_url()
    return RedirectResponse(url)


@router.get("/google")
async def google_auth(code: str,
                      auth_service: AuthService = Depends(get_auth_service),
                      ):
    try:
        user_data = await auth_service.google_auth(code)
        return {"status": "success", "user_data": user_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/login/yandex")
async def yandex_login(auth_service: AuthService = Depends(get_auth_service)):
    url = auth_service.get_yandex_redirect_url()
    return RedirectResponse(url)


@router.get("/yandex")
async def yandex_auth(code: str,
                      auth_service: AuthService = Depends(get_auth_service),
                      ):
    return await auth_service.yandex_auth(code)
