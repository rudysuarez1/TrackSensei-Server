from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from datetime import datetime
from backend.db.db import get_db
from backend.db.models.telemetry import TelemetryPoint
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from backend.api.utils.auth import SECRET_KEY, ALGORITHM
from backend.db.models.users import User
from backend.api.routes.laps import get_current_user
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.api.utils.auth import get_current_user
from backend.db.models.users import User
from backend.api.schemas.telemetry import TelemetryData


def check_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient privileges"
            )
        return current_user

    return role_checker


# @app.get("/some-protected-route")
# def protected_route(current_user: User = Depends(check_role("paid_user"))):
#     return {"message": "Welcome, paid user!"}


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/telemetry/{lap_id}", response_model=dict)
def upload_telemetry(
    lap_id: int,
    data: List[TelemetryData],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    points = [TelemetryPoint(lap_id=lap_id, **point.dict()) for point in data]
    db.add_all(points)
    db.commit()
    return {
        "message": f"{len(points)} telemetry points added to lap {lap_id}",
        "user": current_user.username,
    }


@router.get("/telemetry/{lap_id}", response_model=List[TelemetryData])
def get_telemetry(lap_id: int, db: Session = Depends(get_db)):
    telemetry_points = (
        db.query(TelemetryPoint).filter(TelemetryPoint.lap_id == lap_id).all()
    )
    if not telemetry_points:
        raise HTTPException(
            status_code=404, detail="Telemetry data not found for this lap"
        )
    return telemetry_points
