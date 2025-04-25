from pydantic import BaseModel


class UserPreferences(BaseModel):
    language: str
    theme: str
    notifications_enabled: bool


class SessionManagement(BaseModel):
    default_session_duration: int  # in minutes
    auto_save: bool


class TelemetrySettings(BaseModel):
    data_collection: bool
    data_sharing: bool


class PrivacySettings(BaseModel):
    profile_visibility: str  # e.g., 'public', 'friends', 'private'
    data_retention: int  # in days


class SecuritySettings(BaseModel):
    password_policy: str
    two_factor_auth: bool


class Settings(BaseModel):
    user_preferences: UserPreferences
    session_management: SessionManagement
    telemetry_settings: TelemetrySettings
    privacy_settings: PrivacySettings
    security_settings: SecuritySettings
