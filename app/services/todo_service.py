from sqlalchemy.orm import Session
from app.db.schema import Todo

class TodoService:
  def __init__(self, db: Session):
    self.db = db

  def get_todos(self):
    return self.db.query(Todo).all()