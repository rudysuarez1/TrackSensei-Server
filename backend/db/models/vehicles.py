from sqlalchemy import Column, Integer, String, Float, ForeignKey
from backend.db.models.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    weight_kg = Column(Float)
