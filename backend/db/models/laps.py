from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from .base import Base


class Lap(Base):
    __tablename__ = "laps"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)
    started_at = Column(DateTime, nullable=False)
    duration_ms = Column(Integer)
    conditions = Column(String)  # Store JSON as string for now

    telemetry_points = relationship("TelemetryPoint", back_populates="lap")
