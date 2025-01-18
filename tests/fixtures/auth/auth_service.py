import pytest

from app.users.auth.service import AuthService


@pytest.fixture
def auth_service(yandex_client, google_client, user_logic):
    return AuthService(
        user_logic=user_logic,
        google_client=google_client,
        yandex_client=yandex_client
    )

