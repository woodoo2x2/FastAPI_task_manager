from pydantic import BaseModel, Field


class GoogleUserData(BaseModel):
    id: int
    email: str
    name: str
    access_token: str


class YandexUserData(BaseModel):
    id: int
    email: str = Field(..., alias='default_email')
    name: str = Field(..., alias='real_name')
    access_token: str = Field(..., alias='psuid')
