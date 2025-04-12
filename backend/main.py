from fastapi import FastAPI
from backend.db.models.base import Base
from backend.db.db import engine
from backend.api.routes.laps import router as laps_router
from backend.api.routes.telemetry import router as telemetry_router
from backend.api.routes.users import router as users_router
from backend.api.utils.auth import get_current_user

app = FastAPI()

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(laps_router, prefix="/api", tags=["Laps"])
app.include_router(telemetry_router, prefix="/api", tags=["Telemetry"])
app.include_router(users_router, prefix="/api", tags=["Users"])


@app.get("/")
def root():
    return {"message": "TrackSensei backend is live!"}
