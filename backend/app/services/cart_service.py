from sqlalchemy.orm import Session
from typing import List, Optional

from app.entities.cart import Cart
from app.repositories.cart_repository import CartRepository
from app.repositories.user_repository import UserRepository
from app.entities.cart_item import CartItem
from app.repositories.cart_item_repository import CartItemRepository

def _get_user(db: Session, user_id: int):
    user_repo = UserRepository(db)
    user = user_repo.get_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    return user

def _get_cart(db: Session, user_id: int) -> Cart:
    cart_repo = CartRepository(db)
    return cart_repo.get_or_create_for_user(user_id)

def _get_cart_item_repo(db: Session) -> CartItemRepository:
    return CartItemRepository(db)

def get_cart_service(db: Session, user_id: int) -> Cart:
    _get_user(db, user_id)
    return _get_cart(db, user_id)

def add_to_cart_service(db: Session, user_id: int, product_id: int, quantity: int) -> CartItem:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    existing_item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product_id
    ).first()
    
    if existing_item:
        db.query(CartItem).filter(
            CartItem.id == existing_item.id
        ).update({"quantity": existing_item.quantity + quantity})
        db.commit()
        
        return db.query(CartItem).filter(CartItem.id == existing_item.id).first()
    else:
        new_cart_item = CartItem(
            cart_id=cart.id,
            product_id=product_id,
            quantity=quantity
        )
        db.add(new_cart_item)
        db.commit()
        db.refresh(new_cart_item)
        return new_cart_item

def update_cart_item_service(db: Session, user_id: int, item_id: int, quantity: int) -> Optional[CartItem]:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    cart_item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not cart_item:
        return None
    
    cart_item_cart_id = db.scalar(db.query(CartItem.cart_id).filter(CartItem.id == item_id))
    if cart_item_cart_id != cart.id:
        return None
    
    if quantity <= 0:
        db.delete(cart_item)
        db.commit()
        return None
    
    db.query(CartItem).filter(CartItem.id == item_id).update({"quantity": quantity})
    db.commit()
    
    return db.query(CartItem).filter(CartItem.id == item_id).first()

def remove_from_cart_service(db: Session, user_id: int, item_id: int) -> bool:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    cart_item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not cart_item:
        return False
    
    cart_item_cart_id = db.scalar(db.query(CartItem.cart_id).filter(CartItem.id == item_id))
    if cart_item_cart_id != cart.id:
        return False
    
    db.delete(cart_item)
    db.commit()
    return True

def clear_cart_service(db: Session, user_id: int) -> None:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()
    db.commit()

def add_item_to_cart(db: Session, user_id: int, product_id: int, quantity: int) -> CartItem:
    return add_to_cart_service(db, user_id, product_id, quantity)
    
def remove_item_from_cart(db: Session, user_id: int, product_id: int) -> bool:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    cart_item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product_id
    ).first()
    
    if not cart_item:
        return False
        
    db.delete(cart_item)
    db.commit()
    return True

def list_cart_items(db: Session, user_id: int) -> List[CartItem]:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    return db.query(CartItem).filter(CartItem.cart_id == cart.id).all()

def update_cart_item_quantity(db: Session, user_id: int, product_id: int, quantity: int) -> Optional[CartItem]:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    
    cart_item = db.query(CartItem).filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product_id
    ).first()
    
    if not cart_item:
        return None
        
    if quantity <= 0:
        db.delete(cart_item)
        db.commit()
        return None
    
    db.query(CartItem).filter(CartItem.id == cart_item.id).update({"quantity": quantity})
    db.commit()
    
    return db.query(CartItem).filter(CartItem.id == cart_item.id).first()