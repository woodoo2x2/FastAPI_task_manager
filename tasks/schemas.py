from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int | None = None
    name: str
    pomodoro_count: int
    category_id: int
