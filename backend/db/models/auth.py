from sqlalchemy import Column, String, Integer
from .base import Base


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    token = Column(String, unique=True, index=True)
