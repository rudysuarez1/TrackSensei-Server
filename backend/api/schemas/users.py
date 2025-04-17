from pydantic import BaseModel, EmailStr, constr
from typing import Optional


# User creation schema (input)
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)  # Username with length constraints
    email: EmailStr  # Validated email format
    phone_number: Optional[str] = None  # Optional phone number
    password: constr(min_length=8)  # Password with minimum length

    class Config:
        from_attributes = True  # Allow creation from attributes


# User authentication schema (login)
class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True  # Allow creation from attributes


# User data returned in responses (output)
class UserRead(BaseModel):
    id: int  # User ID
    username: str  # Username
    email: EmailStr  # Validated email format
    phone_number: Optional[str] = None  # Optional phone number
    role: str  # Authorization information (admin, user, paid_user)

    class Config:
        from_attributes = True  # Updated from orm_mode to from_attributes


# class UserSignUpModel(BaseModel):
#     username: constr(min_length=3, max_length=50)  # Username with length constraints
#     email: EmailStr  # Validated email format
#     password: constr(min_length=8)  # Password with minimum length
#     phone_number: Optional[str] = None  # Optional phone number

#     class Config:
#         from_attributes = True  # Allow creation from attributes
