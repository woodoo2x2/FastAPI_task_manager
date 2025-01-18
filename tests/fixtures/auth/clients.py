from dataclasses import dataclass

import httpx
import pytest
from faker import Factory as FakerFactory

from app.settings import Settings
from app.users.auth.schema import GoogleUserData, YandexUserData

faker = FakerFactory.create()


@dataclass
class FakeGoogleClient:
    async_client: httpx.AsyncClient
    settings: Settings

    async def get_user_info(self, code) -> GoogleUserData:
        access_token = self.get_access_token(code)
        return google_user_info()

    def get_access_token(self, code) -> str:
        return f"Fake google access token {code}"


@dataclass
class FakeYandexClient:
    settings: Settings
    async_client: httpx.AsyncClient

    async def get_user_info(self, code) -> dict:
        access_token = await self.get_access_token(code)
        return yandex_user_info()

    async def get_access_token(self, code) -> str:
        return f"Fake yandex access token {code}"


@pytest.fixture
def google_client():
    return FakeGoogleClient(settings=Settings(), async_client=httpx.AsyncClient())


@pytest.fixture
def yandex_client():
    return FakeYandexClient(settings=Settings(), async_client=httpx.AsyncClient())


def google_user_info() -> GoogleUserData:
    return GoogleUserData(
        id=faker.random_int(),
        email=faker.email(),
        name=faker.name(),
        access_token=faker.sha256(),

    )


def yandex_user_info() -> YandexUserData:
    return YandexUserData(
        id=faker.random_int(),
        default_email=faker.email(),
        real_name=faker.name(),
        psuid=faker.sha256(),
    )
