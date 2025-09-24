from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.cart_schema import Cart, CartItem, CartItemCreate, CartItemUpdate
from app.services.cart_service import (
    get_cart_service,           # Changed from get_user_cart_service
    add_item_to_cart,        # This should exist
    update_cart_item_service,   # This should exist  
    remove_from_cart_service,   # This should exist
    clear_cart_service          # This should exist
)
from app.auth.dependencies import get_current_active_user
from app.entities.user import User
from app.utils.db import get_db

router = APIRouter(prefix="/cart", tags=["cart"])

@router.get("/", response_model=Cart)
def get_my_cart(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return get_cart_service(db, current_user.id)  # Updated function name

@router.post("/items", response_model=CartItem, status_code=status.HTTP_201_CREATED)
def add_item_to_cart(
    cart_item: CartItemCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    try:
        return add_item_to_cart(db, current_user.id, cart_item.product_id, cart_item.quantity)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/items/{item_id}", response_model=CartItem)
def update_cart_item(
    item_id: int,
    cart_item_update: CartItemUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    try:
        item = update_cart_item_service(db, current_user.id, item_id, cart_item_update.quantity)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cart item not found"
            )
        return item
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item_from_cart(
    item_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    success = remove_from_cart_service(db, current_user.id, item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found"
        )

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def clear_cart(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    clear_cart_service(db, current_user.id)