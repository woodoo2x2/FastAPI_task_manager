from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Mapped

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String)
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]


class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
