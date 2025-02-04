import pytest

from app.users.auth.service import AuthService
from app.users.logic import UserLogic


@pytest.fixture
def auth_service_mock(yandex_client, google_client, fake_user_logic):
    return AuthService(
        user_logic=fake_user_logic,
        google_client=google_client,
        yandex_client=yandex_client,
    )


@pytest.fixture
def auth_service(yandex_client, google_client, db_session):
    return AuthService(
        user_logic=UserLogic(db_session=db_session),
        yandex_client=yandex_client,
        google_client=google_client,
    )
