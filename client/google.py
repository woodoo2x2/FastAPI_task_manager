from dataclasses import dataclass

import httpx

from auth.schema import GoogleUserData
from settings import Settings


@dataclass
class GoogleClient:
    settings: Settings
    async_client: httpx.AsyncClient

    async def get_user_info(self, code) -> GoogleUserData:
        access_token = self.get_access_token(code)
        async with self.async_client as client:
            user_info = await client.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"}
            )
            user_info = user_info.json()
            return GoogleUserData(id=user_info['sub'],
                                  email=user_info['email'],
                                  name=user_info['name'],
                                  access_token=access_token)

    async def get_access_token(self, code) -> str:
        data = {
            "code": code,
            "client_id": self.settings.GOOGLE_CLIENT_ID,
            "client_secret": self.settings.GOOGLE_SECRET_KEY,
            "redirect_uri": self.settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        with self.async_client as client:
            response = await client.post(self.settings.GOOGLE_TOKEN_URL, data=data)
        return response.json()['access_token']
