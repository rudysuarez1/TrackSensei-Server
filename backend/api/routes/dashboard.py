from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.models.users import User
from backend.db.db import get_db
from backend.api.utils.auth import get_current_user

router = APIRouter()


@router.get("/dashboard")
async def dashboard(current_user: User = Depends(get_current_user)):
    return {"message": f"Welcome to the dashboard, {current_user.username}!"}


@router.get("/dashboard/data")
async def get_dashboard_data(current_user: User = Depends(get_current_user)):
    db = next(get_db())
    total_users = db.query(User).count()
    return {
        "total_users": total_users,
    }
