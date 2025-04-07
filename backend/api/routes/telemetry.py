from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from datetime import datetime
from backend.db.db import get_db
from backend.db.models.telemetry import TelemetryPoint

router = APIRouter()


class TelemetryData(BaseModel):
    timestamp: datetime
    latitude: float
    longitude: float
    speed_kph: float | None = None
    accel_x: float | None = None
    accel_y: float | None = None
    accel_z: float | None = None
    elevation_m: float | None = None


@router.post("/telemetry/{lap_id}")
def upload_telemetry(
    lap_id: int, data: List[TelemetryData], db: Session = Depends(get_db)
):
    points = [TelemetryPoint(lap_id=lap_id, **point.dict()) for point in data]
    db.add_all(points)
    db.commit()
    return {"message": f"{len(points)} telemetry points added to lap {lap_id}"}
