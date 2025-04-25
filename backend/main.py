from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from backend.db.models.base import Base
from backend.db.db import DATABASE_URL
from backend.api.routes.laps import router as laps_router
from backend.api.routes.telemetry import router as telemetry_router
from backend.api.routes.users import router as users_router
from backend.api.routes.sessions import router as sessions_router
from backend.api.routes.auth import router as auth_router
from backend.api.utils.auth import get_current_user
from fastapi.responses import RedirectResponse
from backend.api.routes.dashboard import router as dashboard_router
from backend.db.models.users import User
from backend.api.routes import settings
from backend.db.models.settings import UserSettings

app = FastAPI()

# Create the database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to initialize the database
def init_db():
    # Create an inspector to check for existing tables
    inspector = inspect(engine)

    # List of tables to check
    required_tables = [
        "users",
        "sessions",
        "laps",
        "telemetry_points",
        "tracks",
        "vehicles",
        "user_settings",  # Add the new settings table
    ]

    # Create all tables if they do not exist
    for table in required_tables:
        if table not in inspector.get_table_names():
            print(f"Creating table: {table}")
            Base.metadata.create_all(bind=engine)


# Call the init_db function when starting the app
@app.on_event("startup")
async def startup_event():
    init_db()


# Include routers
app.include_router(laps_router, prefix="/api", tags=["Laps"])
app.include_router(telemetry_router, prefix="/api", tags=["Telemetry"])
app.include_router(users_router, prefix="/api", tags=["Users"])
app.include_router(sessions_router, prefix="/api", tags=["Sessions"])
app.include_router(auth_router, prefix="/api", tags=["Auth"])
app.include_router(dashboard_router, prefix="/api", tags=["Dashboard"])
app.include_router(settings.router, prefix="/api", tags=["settings"])


@app.get("/")
async def root(current_user: User = Depends(get_current_user)):
    # If the user is logged in, redirect to the dashboard
    return RedirectResponse(
        url="/api/dashboard"
    )  # Adjust the URL to your actual dashboard route


# If the user is not logged in, redirect to the login page
@app.get("/login")
def login_page():
    return {
        "message": "Please log in."
    }  # This can be replaced with your actual login page logic
