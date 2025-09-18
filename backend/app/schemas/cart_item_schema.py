from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., gt=0, description="Quantity of the product")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    quantity: Optional[int] = Field(None, gt=0, description="Updated quantity")

class CartItemResponse(CartItemBase):
    id: int
    user_id: int
    product_name: str
    product_price: Decimal
    subtotal: Decimal
    
    class Config:
        from_attributes = True