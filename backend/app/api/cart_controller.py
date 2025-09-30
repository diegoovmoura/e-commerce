from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.cart_schema import Cart, CartItem, CartItemCreate, CartItemUpdate
from app.services.cart_service import (
    get_cart_service,
    add_to_cart_service,
    update_cart_item_service,
    remove_from_cart_service,
    clear_cart_service
)
from app.auth.dependencies import get_current_active_user
from app.entities.user import User
from app.utils.db import get_db

router = APIRouter(prefix="/cart")

@router.get("/", response_model=Cart)
def get_my_cart(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    user_id = db.scalar(db.query(User.id).filter(User.id == current_user.id))
    return get_cart_service(db, user_id)

@router.post("/items", response_model=CartItem, status_code=status.HTTP_201_CREATED)
def add_item_to_cart_endpoint(
    cart_item: CartItemCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    try:
        user_id = db.scalar(db.query(User.id).filter(User.id == current_user.id))
        return add_to_cart_service(db, user_id, cart_item.product_id, cart_item.quantity)
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
        user_id = db.scalar(db.query(User.id).filter(User.id == current_user.id))
        
        if cart_item_update.quantity is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantity is required"
            )
            
        item = update_cart_item_service(db, user_id, item_id, cart_item_update.quantity)
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
    user_id = db.scalar(db.query(User.id).filter(User.id == current_user.id))
    success = remove_from_cart_service(db, user_id, item_id)
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
    user_id = db.scalar(db.query(User.id).filter(User.id == current_user.id))
    clear_cart_service(db, user_id)