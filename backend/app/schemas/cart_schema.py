from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity of the product")
    price: Decimal = Field(..., gt=0, description="Price per unit")

class CartItemCreate(CartItemBase):
    quantity: int = Field(..., gt=0)
    pass

class CartItemUpdate(BaseModel):
    quantity: Optional[int] = Field(None, gt=0)

class CartItem(CartItemBase):
    id: int
    subtotal: Decimal
    
    class Config:
        from_attributes = True

class CartBase(BaseModel):
    user_id: int = Field(..., description="User ID who owns the cart")

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    items: List[CartItem] = []
    total: Decimal = Field(default=Decimal('0.00'))
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CartSummary(BaseModel):
    total_items: int
    total_amount: Decimal
    items_count: int