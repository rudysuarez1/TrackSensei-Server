# backend/api/utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES"))
