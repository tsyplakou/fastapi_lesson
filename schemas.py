from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: datetime


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    deadline: datetime
    completed: bool
    owner_id: int
