from database import get_db
from fastapi import APIRouter, Depends
from models import User
from passlib.hash import bcrypt
from schemas import UserCreate, UserOut
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
