from sqlalchemy import select
from sqlalchemy.orm import Session
from typing_extensions import Sequence

from .model import Task
from .schemas import TaskSchema


class TaskLogic:
    def __init__(self, db: Session):
        self.db_session = db

    def get_task(self, task_id: int):
        with self.db_session as session:
            task = session.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
        return task

    def get_all_tasks(self):
        with self.db_session as session:
            tasks = session.execute(select(Task)).scalars().all()
        return tasks

    def create_task(self, task: TaskSchema) -> None:
        with self.db_session as session:
            task = Task(id=task.id, name=task.name,pomodoro_count=task.pomodoro_count, category_id=task.category_id)
            session.add(task)
            session.commit()

    def delete_task(self, task_id: int) -> None:
        with self.db_session as session:
            query = session.scalar(select(Task).where(Task.id == task_id))
            session.delete(query)
            session.commit()

    def tasks_by_category(self, category_id: int) -> Sequence[Task]:
        with self.db_session as session:
            query = session.execute(select(Task).where(Task.category_id == category_id))
            tasks = query.scalars().all()
            return tasks
