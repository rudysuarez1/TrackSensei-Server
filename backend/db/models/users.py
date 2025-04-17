from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone_number = Column(String, nullable=True)
    role = Column(String, default="user")
