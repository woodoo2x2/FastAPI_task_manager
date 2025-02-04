import json

from redis import asyncio as Redis

from app.tasks.schemas import TaskSchema


class CacheTask:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def get_tasks(self):
        task_json = await self.redis.lrange("tasks", 0, -1)
        return [TaskSchema.model_validate(json.loads(task)) for task in task_json]

    async def set_tasks(self, tasks: list[TaskSchema]):
        json_tasks = [task.json() for task in tasks]
        await self.redis.lpush("tasks", *json_tasks)
