from fastapi import FastAPI

from tasks.router import router as tasks_router

app = FastAPI()

app.include_router(tasks_router)


@app.get("/")
async def mainpage():
    return {"message": "mainpage"}