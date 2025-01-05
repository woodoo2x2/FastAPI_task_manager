from fastapi import FastAPI

from tasks.router import router as tasks_router
from user.router import router as user_router
from auth.router import router as auth_router

app = FastAPI()

app.include_router(tasks_router)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
async def mainpage():
    return {"message": "mainpage"}