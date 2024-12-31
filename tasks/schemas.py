from pydantic import BaseModel

class Task(BaseModel):
    id : str
    name: str
    priority : int
    category_id : int
