from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Annotated

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=8)]
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(UserBase):
    id: int
    full_name: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[EmailStr] = None