from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.api.schemas.settings import Settings
from backend.db.models.settings import UserSettings
from backend.db.db import get_db

router = APIRouter()


@router.get("/settings", response_model=Settings)
async def get_settings(user_id: int, db: Session = Depends(get_db)):
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings


@router.put("/settings", response_model=Settings)
async def update_settings(
    new_settings: Settings, user_id: int, db: Session = Depends(get_db)
):
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    if not settings:
        settings = UserSettings(user_id=user_id, **new_settings.dict())
        db.add(settings)
    else:
        for key, value in new_settings.dict().items():
            setattr(settings, key, value)
    db.commit()
    db.refresh(settings)
    return settings
