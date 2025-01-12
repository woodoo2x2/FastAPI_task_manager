from pydantic import BaseModel


class TaskSchema(BaseModel):

    name: str
    pomodoro_count: int
    category_id: int
    user_id: int

    class Config:
        from_attributes = True

class TaskCreateSchema(BaseModel):
    name: str
    pomodoro_count: int
    category_id: int