from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.db import get_db
from backend.db.models.sessions import Session as SessionModel
from backend.db.models.laps import Lap
from backend.api.utils.auth import get_current_user
from backend.api.schemas.sessions import SessionCreate, SessionRead
from backend.api.schemas.laps import LapCreate, LapRead
from backend.db.models.users import User
from datetime import datetime
from typing import List

router = APIRouter()


@router.post("/sessions", response_model=SessionRead)
def create_session(
    session: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_session = SessionModel(
        user_id=current_user.id, start_time=datetime.utcnow(), details=session.details
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session


@router.post("/sessions/{session_id}/laps", response_model=LapRead)
def create_lap(
    session_id: int,
    lap: LapCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    new_lap = Lap(**lap.dict(), user_id=current_user.id, session_id=session_id)
    db.add(new_lap)
    db.commit()
    db.refresh(new_lap)
    return new_lap


@router.get("/sessions", response_model=List[SessionRead])
def list_sessions(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return db.query(SessionModel).filter(SessionModel.user_id == current_user.id).all()


@router.get("/sessions/{session_id}", response_model=SessionRead)
def get_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.user_id == current_user.id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


# Retrieve all laps for a specific session
@router.get("/sessions/{session_id}/laps", response_model=List[LapRead])
def get_laps_for_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    laps = db.query(Lap).filter(Lap.session_id == session_id).all()
    return laps


@router.put("/sessions/{session_id}", response_model=SessionRead)
def update_session(
    session_id: int,
    session: SessionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session_db = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.user_id == current_user.id)
        .first()
    )
    if not session_db:
        raise HTTPException(status_code=404, detail="Session not found")

    session_db.details = session.details
    db.commit()
    return session_db


@router.delete("/sessions/{session_id}")
def delete_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    session = (
        db.query(SessionModel)
        .filter(SessionModel.id == session_id, SessionModel.user_id == current_user.id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    db.delete(session)
    db.commit()
    return {"detail": "Session deleted successfully"}
