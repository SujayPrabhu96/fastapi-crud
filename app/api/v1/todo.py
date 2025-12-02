from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.todo import TodoRead, TodoCreate
from app.services.todo_service import TodoService
from app.db.db import SessionLocal

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

router = APIRouter(
  prefix="/api/v1",
  tags=["todos"]
)

@router.get("/todos", response_model=list[TodoRead])
def get_todos(db: Session = Depends(get_db)):
  return TodoService(db).get_todos()