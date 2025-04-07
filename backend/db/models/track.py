from sqlalchemy import Column, Integer, String, Float, DateTime, func
from backend.db.models.base import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    length_km = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
