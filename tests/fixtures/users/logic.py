from dataclasses import dataclass

import pytest

from app.users.schemas import UserCreateSchema
from tests.fixtures.users.models import UserProfileFactory


@dataclass
class FakeUserLogic:
    async def get_user_by_email(self, email: str) -> None:
        return None

    async def create_user(self, user: UserCreateSchema) -> None:
        return UserProfileFactory()


@pytest.fixture
def fake_user_logic():
    return FakeUserLogic()
