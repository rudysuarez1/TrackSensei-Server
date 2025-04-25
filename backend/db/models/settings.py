from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, index=True
    )  # Assuming you have a user_id to link settings to a user
    language = Column(String, default="en")
    theme = Column(String, default="light")
    notifications_enabled = Column(Boolean, default=True)
    default_session_duration = Column(Integer, default=60)  # in minutes
    auto_save = Column(Boolean, default=True)
    data_collection = Column(Boolean, default=True)
    data_sharing = Column(Boolean, default=False)
    profile_visibility = Column(
        String, default="public"
    )  # e.g., 'public', 'friends', 'private'
    data_retention = Column(Integer, default=30)  # in days
    password_policy = Column(String, default="strong")
    two_factor_auth = Column(Boolean, default=False)
