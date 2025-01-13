from dataclasses import dataclass

from cache.logic import CacheTask
from tasks.logic import TaskLogic
from tasks.schemas import TaskSchema


@dataclass
class TaskService:
    cache_task: CacheTask
    task_logic: TaskLogic

    async def get_tasks(self):
        if cache_tasks := await self.cache_task.get_tasks():
            return cache_tasks
        else:
            tasks = self.task_logic.get_all_tasks()
            tasks_schema = [TaskSchema.model_validate(task.__dict__) for task in tasks]
            if tasks_schema:
                await self.cache_task.set_tasks(tasks_schema)
            return tasks_schema
