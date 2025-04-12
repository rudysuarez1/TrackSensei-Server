from pydantic import BaseModel, EmailStr


# User creation schema (input)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str  # plain password, hashed on creation

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
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes = True  # Allow creation from attributes


class UserSignUpModel(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True  # Allow creation from attributes
