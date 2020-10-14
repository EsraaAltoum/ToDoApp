from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class TaskCreate(BaseModel):
    task: str
    priority: int
    note: str
    due_date: datetime


