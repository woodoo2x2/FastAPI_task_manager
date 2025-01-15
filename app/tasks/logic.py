from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Sequence

from app.exceptions import TaskNotFoundException
from .model import Task
from .schemas import TaskCreateSchema


class TaskLogic:
    def __init__(self, db: AsyncSession):
        self.db_session = db

    async def get_user_task(self, task_id: int, user_id: int) -> Task | None:
        query = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        async with self.db_session as session:
            task = (await session.execute(query)).scalar_one_or_none()
        return task

    async def get_task(self, task_id: int):
        async with self.db_session as session:
            task = (await session.execute(select(Task).where(Task.id == task_id))).scalar_one_or_none()
        return task

    async def get_all_tasks(self):
        async with self.db_session as session:
            tasks = (await session.execute(select(Task))).scalars().all()
        return tasks

    async def create_task(self, task: TaskCreateSchema, user_id: int) -> int:
        async with self.db_session as session:
            task = Task(name=task.name,
                        pomodoro_count=task.pomodoro_count,
                        category_id=task.category_id,
                        user_id=user_id)
            session.add(task)
            await session.commit()
            return task.id

    async def delete_task(self, task_id: int, user_id: int) -> None:
        task = await self.get_user_task(task_id, user_id)
        if not task:
            raise TaskNotFoundException
        if task.user_id == user_id:
            with self.db_session as session:
                query = session.scalar(select(Task).where(Task.id == task_id))
                session.delete(query)
                session.commit()

    async def tasks_by_category(self, category_id: int) -> Sequence[Task]:
        async with self.db_session as session:
            query = select(Task).where(Task.category_id == category_id)
            tasks = (await session.execute(query)).scalars().all()
            return tasks

    async def update_task(self, task_id: int, name: str, user_id: int) -> Task:
        task = await self.get_user_task(task_id, user_id)
        if not task:
            raise TaskNotFoundException
        task.name = name

        async with self.db_session as session:
            session.add(task)
            await session.commit()
            await session.refresh(task)

        return task
