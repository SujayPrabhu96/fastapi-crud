from fastapi import FastAPI
from app.api.v1.todo import router as todo_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(todo_router)