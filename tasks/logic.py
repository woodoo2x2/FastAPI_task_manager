from sqlalchemy import select
from sqlalchemy.orm import Session
from typing_extensions import Sequence

from exceptions import TaskNotFoundException
from .model import Task
from .schemas import TaskCreateSchema, TaskSchema


class TaskLogic:
    def __init__(self, db: Session):
        self.db_session = db

    def get_user_task(self, task_id: int, user_id: int) -> Task | None:
        query = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        with self.db_session as session:
            task = session.execute(query).scalar_one_or_none()
        return task

    def get_task(self, task_id: int):
        with self.db_session as session:
            task = session.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
        return task

    def get_all_tasks(self):
        with self.db_session as session:
            tasks = session.execute(select(Task)).scalars().all()
        return tasks

    def create_task(self, task: TaskCreateSchema, user_id: int) -> int:
        with self.db_session as session:
            task = Task(name=task.name,
                        pomodoro_count=task.pomodoro_count,
                        category_id=task.category_id,
                        user_id=user_id)
            session.add(task)
            session.commit()
            return task.id

    def delete_task(self, task_id: int, user_id: int) -> None:
        task = self.get_user_task(task_id, user_id)
        if not task:
            raise TaskNotFoundException
        if task.user_id == user_id:
            with self.db_session as session:
                query = session.scalar(select(Task).where(Task.id == task_id))
                session.delete(query)
                session.commit()

    def tasks_by_category(self, category_id: int) -> Sequence[Task]:
        with self.db_session as session:
            query = session.execute(select(Task).where(Task.category_id == category_id))
            tasks = query.scalars().all()
            return tasks

    def update_task(self, task_id: int, name: str, user_id: int) -> TaskSchema:
        task = self.get_user_task(task_id, user_id)
        if not task:
            raise TaskNotFoundException
        task.name = name

        with self.db_session as session:
            session.add(task)
            session.commit()
            session.refresh(task)

        return task
