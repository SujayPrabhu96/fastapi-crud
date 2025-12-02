from fastapi import APIRouter, Depends, HTTPException
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