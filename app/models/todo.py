from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class TodoRead(BaseModel):
  id: int
  title: str
  description: Optional[str] = None
  completed: Optional[bool] = False
  created_at: datetime
  updated_at: datetime

class TodoCreate(BaseModel):
  title: str
  description: Optional[str] = None
  completed: Optional[bool] = False
  created_at: datetime = datetime.now()
  updated_at: datetime = datetime.now()

  @field_validator('completed')
  def validate_is_completed(cls, v):
    if v is True:
      raise ValueError('Todo task should not be completed during creation')
    return v