from typing import List

from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session, sessionmaker

from database import get_db_session
from .model import Task

class TaskLogic:
    def __init__(self):
        self.db_session = get_db_session()

    def get_task(self, task_id: int):
        with self.db_session() as session:
            task = session.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
        return task

    def get_all_tasks(self):
        with self.db_session as session:
            tasks = session.execute(select(Task)).scalars().all()
        return tasks

    def create_task(self, task: Task) -> None:
        with self.db_session() as session:
            session.add(task)
            session.commit()

    def delete_task(self, task_id: int) -> None:
        with self.db_session() as session:
            query = session.scalar(select(Task).where(Task.id == task_id))
            session.delete(query)
            session.commit()

    def tasks_by_category(self, category_id: int) -> List[Task]:
        with self.db_session() as session:
            query = session.execute(select(Task).where(Task.category_id == category_id))
            tasks = query.scalars().all()
            return tasks
