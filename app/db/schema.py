from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.db import Base
from datetime import datetime

class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  completed = Column(Boolean, default=False)
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now)