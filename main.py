from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def mainpage():
    return {"message": "mainpage"}