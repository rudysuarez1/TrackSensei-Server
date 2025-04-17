from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class LapBase(BaseModel):
    user_id: int
    session_id: int
    vehicle_id: int
    track_id: int
    started_at: datetime
    duration_ms: Optional[int] = None
    conditions: Optional[str] = None  # Store JSON as string for now


class LapCreate(LapBase):
    pass


class LapRead(LapBase):
    id: int

    class Config:
        from_attributes = True
