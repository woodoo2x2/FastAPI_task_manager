import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env")


class Settings(BaseSettings):
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    DATABASE_HOST: str = os.getenv('DATABASE_HOST')
    DATABASE_USER: str = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
    DATABASE_PORT: str = os.getenv('DATABASE_PORT')

    REDIS_HOST: str = os.getenv('REDIS_HOST')
    REDIS_PORT: str = os.getenv('REDIS_PORT')
    REDIS_DB: str = os.getenv('REDIS_DB')

    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_DECODE_ALGORITHM: str = os.getenv('JWT_ALGORITHM')

    GOOGLE_CLIENT_ID: str = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_REDIRECT_URI: str = os.getenv('GOOGLE_REDIRECT_URI')
    GOOGLE_SECRET_KEY : str = os.getenv('GOOGLE_SECRET_KEY')
    GOOGLE_TOKEN_URL : str = os.getenv('GOOGLE_TOKEN_URI')
    @property
    def google_redirect_url(self) -> str:
        return f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={self.GOOGLE_CLIENT_ID}&redirect_uri={self.GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
