from dataclasses import dataclass

from app.users.auth.service import AuthService
from app.users.logic import UserLogic
from app.users.schemas import UserLoginSchema, UserCreateSchema


@dataclass
class UserService:
    user_logic: UserLogic
    auth_service: AuthService

    async def create_user(self, data: UserCreateSchema) -> UserLoginSchema:
        user = await self.user_logic.create_user(data)
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)
