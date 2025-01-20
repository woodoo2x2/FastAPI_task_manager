from dataclasses import dataclass

from app.users.auth.client.mail import MailClient
from app.users.auth.service import AuthService
from app.users.logic import UserLogic
from app.users.schemas import UserLoginSchema, UserCreateSchema


@dataclass
class UserService:
    user_logic: UserLogic
    auth_service: AuthService
    mail_client: MailClient

    async def create_user(self, data: UserCreateSchema) -> UserLoginSchema:
        user = await self.user_logic.create_user(data)
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        if user.email:
            self.mail_client.send_mail(to=data.email)
        return UserLoginSchema(user_id=user.id, access_token=access_token)
