from dataclasses import dataclass

import httpx

from app.users.auth.schema import GoogleUserData
from app.settings import Settings


@dataclass
class GoogleClient:
    settings: Settings
    async_client: httpx.AsyncClient

    async def get_user_info(self, code) -> GoogleUserData:
        access_token = await self.get_access_token(code)

        user_info = await self.async_client.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        user_info = user_info.json()

        return GoogleUserData(
            id=user_info["sub"],
            email=user_info["email"],
            name=user_info["name"],
            access_token=access_token,
        )

    async def get_access_token(self, code) -> str:
        data = {
            "code": code,
            "client_id": self.settings.GOOGLE_CLIENT_ID,
            "client_secret": self.settings.GOOGLE_SECRET_KEY,
            "redirect_uri": self.settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        response = await self.async_client.post(
            self.settings.GOOGLE_TOKEN_URL,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code != 200:
            error_message = response.json().get("error_description", response.text)
            raise Exception(f"Failed to get access token: {error_message}")

        return response.json().get("access_token")
