from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.db.models.users import User
from backend.api.utils.auth import get_password_hash
from backend.api.schemas.users import UserCreate, UserRead

router = APIRouter()


# User Registration
@router.post("/users", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        phone_number=user.phone_number,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Update User Information
@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = user_data.username
    user.email = user_data.email
    user.hashed_password = get_password_hash(user_data.password)
    user.phone_number = user_data.phone_number
    db.commit()
    db.refresh(user)
    return user


# Get User by ID
@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# User Delete (Delete User by ID)
@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
