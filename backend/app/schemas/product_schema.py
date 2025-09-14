from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(BaseModel):
    business_id: int
    name: str
    description: str
    price: float
    stock: int

class ProductOut(ProductCreate):
    id: int

    class Config:
        orm_mode = True

class ProductUpdate(ProductBase):
    quantity: Optional[int] = None
    stock: Optional[int] = None
    price: Optional[float] = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class ProductList(BaseModel):
    products: List[Product]