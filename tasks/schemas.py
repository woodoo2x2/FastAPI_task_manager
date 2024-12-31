from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    priority: int
    category_id: int
