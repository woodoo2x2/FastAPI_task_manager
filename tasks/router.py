from fastapi import APIRouter, Depends
from redis import Redis

from cache.access import get_redis_connection
from database import Session, get_db_session
from tasks.logic import TaskLogic
from tasks.schemas import TaskSchema
from cache.logic import CacheTask

router = APIRouter(prefix="/tasks", tags=["tasks"])



@router.get("/")
async def get_all_tasks(db: Session = Depends(get_db_session),
                        redis: Redis = Depends(get_redis_connection)):
    tasks_logic = TaskLogic(db)
    tasks = tasks_logic.get_all_tasks()

    if tasks:
        return tasks
    else:
        cache = CacheTask(redis)


        tasks_schema = [TaskSchema.model_validate(task.__dict__) for task in tasks]

        cache.set_tasks(tasks_schema)
        return tasks_schema

@router.get("/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    return tasks_logic.get_task(task_id)

@router.post("/")
async def create_task(task: TaskSchema, db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    task_id = tasks_logic.create_task(task)
    return {"message": f"Task with id - {task_id} created successfully"}

@router.delete("/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db_session)):
    tasks_logic = TaskLogic(db)
    tasks_logic.delete_task(task_id)
    return {"message": "Task deleted successfully"}
