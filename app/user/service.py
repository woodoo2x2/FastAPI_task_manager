from dataclasses import dataclass

from app.auth.service import AuthService
from app.user.logic import UserLogic
from app.user.schemas import UserLoginSchema


@dataclass
class UserService:
    user_logic: UserLogic
    auth_service: AuthService

    async def create_user(self, username: str, password: str) -> UserLoginSchema:
        print(username,password, "ASSASDASDS")
        user = await self.user_logic.create_user(username, password)
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)
