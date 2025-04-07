from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.db.models.lap import Lap
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class LapCreate(BaseModel):
    user_id: int
    vehicle_id: int
    track_id: int
    started_at: datetime
    duration_ms: int
    conditions: str | None = None


@router.post("/laps")
def create_lap(lap: LapCreate, db: Session = Depends(get_db)):
    db_lap = Lap(**lap.dict())
    db.add(db_lap)
    db.commit()
    db.refresh(db_lap)
    return db_lap
