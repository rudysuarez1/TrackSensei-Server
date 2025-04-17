from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from backend.db.db import get_db
from backend.db.models.users import User
from backend.api.utils.auth import (
    verify_password,
    create_access_token,
    create_refresh_token,
    get_current_user,
)
from backend.api.schemas.auth import store_refresh_token, invalidate_refresh_token
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from backend.api.utils.config import SECRET_KEY, ALGORITHM
from backend.api.schemas.users import UserRead

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


class UserLogin(BaseModel):
    username: str
    password: str


@router.post("/auth/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_login.username).first()

    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(user.username)
    refresh_token = create_refresh_token(user.username)

    # Store the refresh token in the database
    store_refresh_token(user.username, refresh_token, db)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/auth/logout")
def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Invalidate the refresh token
    invalidate_refresh_token(token, db)
    return {"detail": "Logout successful"}


@router.post("/auth/refresh")
def refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    # Verify the refresh token and get the username
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Invalid refresh token")
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid refresh token")

    # Create new access token
    new_access_token = create_access_token(username)

    return {"access_token": new_access_token, "token_type": "bearer"}


@router.get("/auth/me", response_model=UserRead)
def read_users_me(current_user: User = Depends(get_current_user)):
    return UserRead.from_orm(current_user)
