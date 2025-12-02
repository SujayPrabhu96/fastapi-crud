from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.models.todo import TodoRead, TodoCreate
from app.services.todo_service import TodoService
from app.db.db import get_db

router = APIRouter(
  prefix="/api/v1",
  tags=["todos"]
)

@router.get("/todos", response_model=list[TodoRead])
def get_todos(db: Session = Depends(get_db)):
  return TodoService(db).get_todos()

@router.post("/todos", response_model=TodoCreate)
def create_todo(todo: TodoCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
  return TodoService(db).create_todo(todo, background_tasks)

@router.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoRead, db: Session = Depends(get_db)):
  return TodoService(db).update_todo(todo_id, todo)

@router.put("/todos/{todo_id}/toggle", response_model=TodoRead)
def toggle_todo(todo_id: int, db: Session = Depends(get_db)):
  return TodoService(db).toggle_todo(todo_id)

@router.delete("/todos/{todo_id}", response_model=TodoRead)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
  return TodoService(db).delete_todo(todo_id)