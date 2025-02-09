from database import SessionLocal
from fastapi import APIRouter, Depends
from models import Task
from schemas import TaskCreate, TaskOut
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from crud import get_tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/", response_model=list[TaskOut])
def get_tasks(user_id: int, db: Session = Depends(get_db)):
    return get_tasks(db, user_id)
