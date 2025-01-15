from fastapi import FastAPI

from app.tasks.router import router as tasks_router
from app.users.router import router as user_router
from app.users.auth.router import router as auth_router

app = FastAPI()

app.include_router(tasks_router)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
async def mainpage():
    return {"message": "mainpage"}