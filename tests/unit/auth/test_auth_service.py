import datetime

import pytest
from jose import jwt

from app.settings import Settings
from app.users.auth.service import AuthService
from app.users.models import UserProfile
from app.users.schemas import UserLoginSchema

pytestmark = pytest.mark.asyncio


async def test_get_google_url__success(auth_service: AuthService, settings: Settings):
    settings_google_redirect_url = settings.google_redirect_url

    auth_service_google_url = auth_service.get_google_redirect_url()

    assert settings_google_redirect_url == auth_service_google_url


async def test_get_yandex_url__success(auth_service: AuthService, settings: Settings):
    settings_yandex_redirect_url = settings.yandex_redirect_url

    auth_service_yandex_url = auth_service.get_yandex_redirect_url()

    assert settings_yandex_redirect_url == auth_service_yandex_url


async def test_generate_jwt_token__success(auth_service: AuthService, settings: Settings):
    user_id = 1
    access_token = auth_service.generate_access_token(user_id)

    decode_access_token = jwt.decode(access_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_DECODE_ALGORITHM])
    decode_user_id = decode_access_token['user_id']
    decode_expire = datetime.datetime.fromtimestamp(decode_access_token['expire'], tz=datetime.timezone.utc)

    assert decode_expire - datetime.datetime.now(tz=datetime.timezone.utc) > datetime.timedelta(days=6)
    assert decode_user_id == user_id


async def test_get_user_id_from_jwt_token__success(auth_service: AuthService, settings: Settings):
    user_id = 1
    access_token = auth_service.generate_access_token(user_id)

    decode_access_token = jwt.decode(access_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_DECODE_ALGORITHM])
    decode_user_id = decode_access_token['user_id']

    assert decode_user_id == user_id


async def test_google_auth__success(auth_service: AuthService, google_client, settings: Settings):
    user = await auth_service.google_auth(code="fake_code")
    user_id = user.user_id
    access_token = auth_service.generate_access_token(user_id)
    decode_access_token = jwt.decode(access_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_DECODE_ALGORITHM])
    decode_user_id = decode_access_token['user_id']

    assert decode_user_id == user_id
    assert isinstance(user, UserLoginSchema)


async def test_yandex_auth__success(auth_service: AuthService, yandex_client, settings: Settings):
    user = await auth_service.yandex_auth(code="fake_code")
