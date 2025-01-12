from fastapi import Depends

from database import Session, get_db_session
from tasks.logic import TaskLogic


def get_task_logic(db: Session = Depends(get_db_session)):
    return TaskLogic(db)
