# backend/api/schemas/auth.py
from sqlalchemy.orm import Session
from backend.db.models.auth import RefreshToken


def store_refresh_token(username: str, token: str, db: Session):
    db_token = RefreshToken(username=username, token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)


def invalidate_refresh_token(token: str, db: Session):
    db.query(RefreshToken).filter(RefreshToken.token == token).delete()
    db.commit()
