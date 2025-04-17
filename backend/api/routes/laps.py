from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.db.models.laps import Lap
from backend.api.utils.auth import get_current_user
from backend.api.schemas.laps import (
    LapCreate,
    LapRead,
)  # Assuming you will create these schemas
from typing import List
from backend.db.models.users import User  # Ensure this import is present

router = APIRouter()


# Retrieve details of a specific lap
@router.get("/laps/{lap_id}", response_model=LapRead)
def get_lap(
    lap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> LapRead:
    lap = db.query(Lap).filter(Lap.id == lap_id).first()
    if not lap:
        raise HTTPException(status_code=404, detail="Lap not found")
    return lap


# Update lap information
@router.put("/laps/{lap_id}", response_model=LapRead)
def update_lap(
    lap_id: int,
    lap: LapCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> LapRead:
    lap_db = db.query(Lap).filter(Lap.id == lap_id).first()
    if not lap_db:
        raise HTTPException(status_code=404, detail="Lap not found")

    for key, value in lap.dict().items():
        setattr(lap_db, key, value)

    db.commit()
    return lap_db


# Delete a lap
@router.delete("/laps/{lap_id}", status_code=204)
def delete_lap(
    lap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lap = db.query(Lap).filter(Lap.id == lap_id).first()
    if not lap:
        raise HTTPException(status_code=404, detail="Lap not found")

    db.delete(lap)
    db.commit()
    return {"detail": "Lap deleted successfully"}
