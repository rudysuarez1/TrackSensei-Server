from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class TelemetryPoint(Base):
    __tablename__ = "telemetry_points"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lap_id = Column(Integer, ForeignKey("laps.id"))
    timestamp = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    speed_kph = Column(Float, nullable=True)
    accel_x = Column(Float, nullable=True)
    accel_y = Column(Float, nullable=True)
    accel_z = Column(Float, nullable=True)
    elevation_m = Column(Float, nullable=True)

    lap = relationship("Lap", back_populates="telemetry_points")
