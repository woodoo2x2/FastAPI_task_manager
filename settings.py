import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env")

class Settings(BaseSettings):
    DATABASE_NAME : str = os.getenv('DATABASE_NAME')
    DATABASE_HOST : str = os.getenv('DATABASE_HOST')
    DATABASE_USER : str = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD : str = os.getenv('DATABASE_PASSWORD')
    DATABASE_PORT : str = os.getenv('DATABASE_PORT')

    REDIS_HOST : str = os.getenv('REDIS_HOST')
    REDIS_PORT : str = os.getenv('REDIS_PORT')
    REDIS_DB : str = os.getenv('REDIS_DB')
