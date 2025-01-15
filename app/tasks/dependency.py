from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.cache.access import get_redis_connection
from app.cache.logic import CacheTask
from app.database.database import get_db_session
from app.tasks.logic import TaskLogic
from app.tasks.service import TaskService


async def get_task_logic(db: AsyncSession = Depends(get_db_session)):
    return TaskLogic(db)


async def get_cache_logic(redis_conn=Depends(get_redis_connection)):
    return CacheTask(redis_conn)


async def get_task_service(cache_task: CacheTask = Depends(get_cache_logic),
                           task_logic: TaskLogic = Depends(get_task_logic)):
    return TaskService(cache_task, task_logic)
