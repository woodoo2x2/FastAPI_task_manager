from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from settings import Settings

settings = Settings()

Base = declarative_base()

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}",
    pool_pre_ping=True,
    future=True,
    echo=True
)

AsyncSessionFactory = async_sessionmaker(engine,
                                         autoflush=False,
                                         expire_on_commit=False)


async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session
