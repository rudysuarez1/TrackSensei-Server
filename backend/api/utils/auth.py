from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.api.utils.config import SECRET_KEY, ALGORITHM, EXPIRATION_MINUTES
from backend.db.models.users import User
from fastapi.security import OAuth2PasswordBearer
from backend.db.models.auth import RefreshToken

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

REFRESH_EXPIRATION_MINUTES = 120  # Set refresh token expiration time


def create_access_token(username: str):
    # Token creation logic
    pass


def create_refresh_token(username: str):
    # Token creation logic
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password using bcrypt."""
    return pwd_context.hash(password)


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception

    return user


def store_refresh_token(username: str, token: str, db: Session):
    db_token = RefreshToken(username=username, token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)


def invalidate_refresh_token(token: str, db: Session):
    db.query(RefreshToken).filter(RefreshToken.token == token).delete()
    db.commit()
