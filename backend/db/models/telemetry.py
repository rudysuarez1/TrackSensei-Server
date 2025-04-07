from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from backend.db.models.base import Base


class TelemetryPoint(Base):
    __tablename__ = "telemetry_points"

    id = Column(Integer, primary_key=True, index=True)
    lap_id = Column(Integer, ForeignKey("laps.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    speed_kph = Column(Float)
    accel_x = Column(Float)
    accel_y = Column(Float)
    accel_z = Column(Float)
    elevation_m = Column(Float)
