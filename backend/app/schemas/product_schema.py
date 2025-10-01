from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class ProductBase(BaseModel):
    name: str = Field(..., max_length=255, description="Product name")
    description: str = Field(..., description="Product description")
    price: Decimal = Field(..., gt=0, description="Product price")
    stock: int = Field(..., ge=0, description="Available stock quantity")
    business_id: int = Field(..., description="Business/Vendor ID")
    image_url: Optional[str] = Field(None, description="Product image URL")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    image_url: Optional[str] = None

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProductSummary(BaseModel):
    id: int
    name: str
    price: Decimal
    stock: int
    
    class Config:
        from_attributes = True

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class ProductList(BaseModel):
    products: List[Product]