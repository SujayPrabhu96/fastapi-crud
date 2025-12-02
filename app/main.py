from fastapi import FastAPI
from app.api.v1.todo import router as todo_router
from app.core.config import config

app = FastAPI(title=config.app_name)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(todo_router)