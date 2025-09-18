from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class BusinessBase(BaseModel):
    name: str = Field(..., max_length=255, description="Business name")
    description: Optional[str] = Field(None, description="Business description")
    email: Optional[str] = Field(None, description="Business contact email")
    phone: Optional[str] = Field(None, description="Business contact phone")

class BusinessCreate(BusinessBase):
    pass

class BusinessUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class Business(BusinessBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class BusinessSummary(BaseModel):
    id: int
    name: str
    description: Optional[str]
    
    class Config:
        from_attributes = True