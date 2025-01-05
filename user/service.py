import string
from dataclasses import dataclass
import random

from user.schemas import UserLoginSchema
from user.logic import UserLogic


@dataclass
class UserService:
    user_logic : UserLogic

    def create_user(self, username: str, password: str) -> UserLoginSchema:
        access_token = self._generate_access_token()
        user = self.user_logic.create_user(username, password, access_token)
        return UserLoginSchema(user_id = user.id, access_token=user.access_token)
    @staticmethod
    def _generate_access_token() -> str:
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))