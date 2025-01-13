from dataclasses import dataclass

import requests

from auth.schema import YandexUserData
from settings import Settings


@dataclass
class YandexClient:
    settings: Settings

    def get_user_info(self, code) -> YandexUserData:
        access_token = self.get_access_token(code)
        user_info = requests.get(
            "https://login.yandex.ru/info?format=json",
            headers={"Authorization": f"OAuth {access_token}"}
        )
        return YandexUserData(**user_info.json(), access_token=access_token)



    def get_access_token(self, code) -> str:
        response = requests.post(
            self.settings.YANDEX_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": self.settings.YANDEX_CLIENT_ID,
                "client_secret": self.settings.YANDEX_SECRET_KEY,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )
        return response.json()['access_token']
