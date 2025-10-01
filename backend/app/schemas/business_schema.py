from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class BusinessBase(BaseModel):
    name: str = Field(..., max_length=255, description="Business name")
    contact_email: Optional[str] = Field(None, description="Business contact email")
    phone_number: Optional[str] = Field(None, description="Business contact phone")
    address: Optional[str] = Field(None, description="Business address")

class BusinessCreate(BusinessBase):
    pass

class BusinessUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    contact_email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

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