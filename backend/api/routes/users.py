from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.db.models.user import User
from pydantic import BaseModel, EmailStr

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: EmailStr


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter((User.username == user.username) | (User.email == user.email))
        .first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
