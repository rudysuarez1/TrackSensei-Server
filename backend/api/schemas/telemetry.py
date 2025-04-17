from pydantic import BaseModel
from datetime import datetime


class TelemetryData(BaseModel):
    timestamp: float
    latitude: float
    longitude: float
    speed_kph: float | None = None
    accel_x: float | None = None
    accel_y: float | None = None
    accel_z: float | None = None
    elevation_m: float | None = None
