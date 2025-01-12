from dataclasses import dataclass
from datetime import datetime, timedelta

from jose import jwt

from exceptions import UserNotFoundException, UserNotCorrectPasswordException, TokenExpiredException, \
    TokenNotCorrectException
from settings import Settings
from user.logic import UserLogic
from user.models import UserProfile
from user.schemas import UserLoginSchema

settings = Settings()


@dataclass
class AuthService:
    user_logic: UserLogic

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_logic.get_user_by_username(username)
        self._validate_user(user, password)
        access_token = self.generate_access_token(user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    @staticmethod
    def _validate_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException

    @staticmethod
    def generate_access_token(user_id: int) -> str:
        expire_time_unix = (datetime.utcnow() + timedelta(days=7)).timestamp()
        token = jwt.encode({'user_id': user_id, 'expire': expire_time_unix},
                           settings.JWT_SECRET_KEY,
                           algorithm=settings.JWT_DECODE_ALGORITHM)
        return token

    @staticmethod
    def get_user_id_from_token(token: str) -> int:
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_DECODE_ALGORITHM])
        except:
            raise TokenNotCorrectException
        if payload['expire'] > (datetime.utcnow() + timedelta(days=7)).timestamp():
            raise TokenExpiredException
        return payload['user_id']
