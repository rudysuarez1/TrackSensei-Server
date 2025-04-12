from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.db.models.users import User
from backend.api.utils.auth import get_password_hash, verify_password
from backend.api.routes.laps import get_current_user
from backend.api.schemas.users import UserCreate, UserRead, UserLogin

router = APIRouter()


#
@router.post("/auth/login", response_model=UserRead)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Check if user exists
    existing_user = (
        db.query(User)
        .filter((User.username == user.username) | (User.email == user.email))
        .first()
    )

    if not existing_user or not verify_password(
        user.password, existing_user.hashed_password
    ):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return existing_user


@router.get("/users/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# New User registration
@router.post("/auth/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user with same username or email already exists
    existing_user = (
        db.query(User)
        .filter((User.username == user.username) | (User.email == user.email))
        .first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    # Hash the provided password
    hashed_pw = get_password_hash(user.password)

    # Create a new user with the default role 'user'
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw,
        role="user",  # default role for new sign ups
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
