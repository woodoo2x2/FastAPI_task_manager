from fastapi import Depends

from cache.access import get_redis_connection
from cache.logic import CacheTask
from database import Session, get_db_session
from tasks.logic import TaskLogic
from tasks.service import TaskService


def get_task_logic(db: Session = Depends(get_db_session)):
    return TaskLogic(db)


def get_cache_logic(redis_conn = Depends(get_redis_connection)):
    return CacheTask(redis_conn)


def get_task_service(cache_task: CacheTask = Depends(get_cache_logic),
                     task_logic: TaskLogic = Depends(get_task_logic)):
    return TaskService(cache_task, task_logic)
