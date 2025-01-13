from pydantic import BaseModel


class GoogleUserData(BaseModel):
    id: int
    email: str
    name: str
    access_token: str
