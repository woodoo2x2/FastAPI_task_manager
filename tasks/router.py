from fastapi import APIRouter, Depends

from database import Session, get_db_session
from tasks.logic import TaskLogic
from tasks.schemas import TaskSchema

router = APIRouter(prefix="/tasks", tags=["tasks"])



@router.get("/")
async def get_all_tasks(db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    return tasks_logic.get_all_tasks()

@router.get("/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    return tasks_logic.get_task(task_id)

@router.post("/")
async def create_task(task: TaskSchema, db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    tasks_logic.create_task(task)
    return {"message": "Task created successfully"}

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    tasks_logic.delete_task(task_id)
    return {"message": "Task deleted successfully"}
