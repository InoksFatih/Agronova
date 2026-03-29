from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReminderCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime


class ReminderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None


class ReminderResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: datetime
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True