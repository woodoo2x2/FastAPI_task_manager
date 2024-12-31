from fastapi import APIRouter

from tasks.schemas import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
async def get_all_tasks():
    return []

@router.post("/")
async def create_task(task: Task):
    return {"message": "Task created"}