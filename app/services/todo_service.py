from fastapi import HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.schema import Todo
from app.models.todo import TodoRead, TodoCreate
from app.services.mail_service import MailService

class TodoService:
  def __init__(self, db: Session):
    self.db = db

  def get_todos(self):
    return self.db.query(Todo).all()

  def create_todo(self, todo: TodoCreate, background_tasks: BackgroundTasks):
    self.db.add(todo)
    self.db.commit()
    self.db.refresh(todo)
    background_tasks.add_task(MailService.send_todo_notification, "sujay@codemancers.com", todo.title, "created")
    return todo

  def update_todo(self, todo_id: int, todo: TodoRead):
    todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
      raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = todo.title
    todo.description = todo.description
    todo.completed = todo.completed
    self.db.commit()
    self.db.refresh(todo)
    return todo

  def toggle_todo(self, todo_id: int):
    todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
      raise HTTPException(status_code=404, detail="Todo not found")
    todo.completed = not todo.completed
    self.db.commit()
    self.db.refresh(todo)
    return todo

  def delete_todo(self, todo_id: int):
    todo = self.db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
      raise HTTPException(status_code=404, detail="Todo not found")
    self.db.delete(todo)
    self.db.commit()
    return todo