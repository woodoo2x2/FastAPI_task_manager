from fastapi import Depends, security, Security, Request, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from auth.service import AuthService
from client.google import GoogleClient
from client.yandex import YandexClient
from database import get_db_session
from exceptions import TokenExpiredException, TokenNotCorrectException
from settings import Settings
from user.logic import UserLogic
from user.service import UserService


def get_yandex_client() -> YandexClient:
    return YandexClient(settings=Settings())


def get_google_client() -> GoogleClient:
    return GoogleClient(settings=Settings())


def get_user_logic(db_session: Session = Depends(get_db_session)) -> UserLogic:
    return UserLogic(db_session=db_session)


def get_auth_service(user_logic: UserLogic = Depends(get_user_logic),
                     google_client: GoogleClient = Depends(get_google_client),
                     yandex_client: YandexClient = Depends(get_yandex_client)) -> AuthService:
    return AuthService(user_logic, google_client, yandex_client)


def get_user_service(user_logic: UserLogic = Depends(get_user_logic),
                     auth_service: AuthService = Depends(get_auth_service)) -> UserService:
    return UserService(user_logic=user_logic, auth_service=auth_service)


reusable_oauth2 = security.HTTPBearer()


def get_request_user_id(request: Request,
                        auth_service: AuthService = Depends(get_auth_service),
                        token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
                        ) -> int:
    try:
        user_id = auth_service.get_user_id_from_token(token.credentials)
    except TokenExpiredException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    except TokenNotCorrectException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    return user_id
