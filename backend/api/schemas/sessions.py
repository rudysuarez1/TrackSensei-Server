from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional


class SessionBase(BaseModel):
    details: Optional[str] = None


class SessionCreate(SessionBase):
    details: constr(min_length=1)  # Ensure details are not empty


class SessionRead(SessionBase):
    id: int
    user_id: int
    start_time: datetime
    end_time: Optional[datetime] = None

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models
