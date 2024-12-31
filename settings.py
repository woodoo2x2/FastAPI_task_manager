import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env")

class Settings(BaseSettings):
    DATABASE_NAME : str = os.getenv('DATABASE_NAME')