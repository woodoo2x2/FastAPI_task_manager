from app.dependency import get_auth_service
from app.users.auth.service import AuthService
import pytest


pytestmark = pytest.mark.asyncio

async def test_get_google_url__success():
    auth_service = await get_auth_service()
    assert isinstance(auth_service, AuthService)


def test_get_google_url__fail():
    pass
