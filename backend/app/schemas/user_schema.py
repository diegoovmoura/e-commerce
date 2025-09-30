from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: EmailStr = Field(..., description="User email address")
    full_name: Optional[str] = Field(None, max_length=255, description="Full name")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="User password")

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None

class PasswordChange(BaseModel):
    old_password: str = Field(..., min_length=6, description="Old password")
    new_password: str = Field(..., min_length=6, description="New password")

class User(UserBase):
    id: int
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserProfile(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str]
    is_active: bool
    
    class Config:
        from_attributes = True