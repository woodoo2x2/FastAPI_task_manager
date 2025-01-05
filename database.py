from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import Settings

settings = Settings()

Base = declarative_base()

engine = create_engine(
    f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
)

Session = sessionmaker(engine)


def get_db_session():
    with Session() as session:
        yield session

