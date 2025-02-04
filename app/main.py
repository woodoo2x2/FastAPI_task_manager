from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.dependency import get_broker_consumer
from app.tasks.router import router as tasks_router
from app.users.auth.router import router as auth_router
from app.users.router import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    #broker_consumer = await get_broker_consumer()
    #await broker_consumer.consume_callback_message()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)
app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
async def mainpage():
    return {"message": "mainpage"}
