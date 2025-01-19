import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv("./.env")


class Settings(BaseSettings):
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    DATABASE_HOST: str = os.getenv('DATABASE_HOST')
    DATABASE_USER: str = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
    DATABASE_PORT: str = os.getenv('DATABASE_PORT')

    REDIS_HOST: str = os.getenv('REDIS_HOST')
    REDIS_PORT: int = os.getenv('REDIS_PORT')
    REDIS_DB: str = os.getenv('REDIS_DB')

    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_DECODE_ALGORITHM: str = os.getenv('JWT_ALGORITHM')

    GOOGLE_CLIENT_ID: str = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_REDIRECT_URI: str = os.getenv('GOOGLE_REDIRECT_URI')
    GOOGLE_SECRET_KEY: str = os.getenv('GOOGLE_SECRET_KEY')
    GOOGLE_TOKEN_URL: str = 'https://accounts.google.com/o/oauth2/token'

    YANDEX_CLIENT_ID: str = os.getenv('YANDEX_CLIENT_ID')
    YANDEX_REDIRECT_URI: str = os.getenv('YANDEX_REDIRECT_URI')
    YANDEX_SECRET_KEY: str = os.getenv('YANDEX_SECRET_KEY')
    YANDEX_TOKEN_URL: str = 'https://oauth.yandex.ru/token'

    CELERY_REDIS_URL: str = os.getenv('CELERY_REDIS_URL')

    MAIL_SERVER: str = os.getenv('MAIL_SERVER')
    MAIL_PORT: int = os.getenv('MAIL_PORT')
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = True
    MAIL_USE_CREDENTIALS: bool = True
    MAIL_USERNAME: str = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD: str = os.getenv('MAIL_PASSWORD')
    MAIL_FROM: str = os.getenv('MAIL_USERNAME')

    @property
    def google_redirect_url(self) -> str:
        return f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"

    @property
    def yandex_redirect_url(self) -> str:
        return (
            f"https://oauth.yandex.ru/authorize?response_type=code&client_id={self.YANDEX_CLIENT_ID}&force_confirm=yes"
        )
