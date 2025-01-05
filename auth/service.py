from dataclasses import dataclass

from exceptions import UserNotFoundException, UserNotCorrectPasswordException
from user.logic import UserLogic
from user.models import UserProfile
from user.schemas import UserLoginSchema

@dataclass
class AuthService:
    user_logic : UserLogic

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_logic.get_user_by_username(username)
        self._validate_user(user, password)
        return UserLoginSchema(user_id = user.id,access_token = user.access_token)

    @staticmethod
    def _validate_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException