from sqlalchemy.orm import Session

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

def _get_cart(db: Session, user_id: int):
    cart_repo = CartRepository(db)
    return cart_repo.get_or_create_for_user(user_id)

def _get_cart_item_repo(db: Session):
    return CartItemRepository(db)

def add_item_to_cart(db: Session, user_id: int, product_id: int, quantity: int) -> CartItem:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    cart_item_repo = _get_cart_item_repo(db)
    cart_item = cart_item_repo.get_by_cart_and_product(cart.id, product_id)
    if cart_item:
        cart_item.quantity += quantity
        return cart_item_repo.update(cart_item)
    else:
        new_cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        return cart_item_repo.create(new_cart_item)
    
def remove_item_from_cart(db: Session, user_id: int, product_id: int) -> bool:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    cart_item_repo = _get_cart_item_repo(db)
    cart_item = cart_item_repo.get_by_cart_and_product(cart.id, product_id)
    if not cart_item:
        return False
    cart_item_repo.delete(cart_item)
    return True

def list_cart_items(db: Session, user_id: int) -> list[CartItem]:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    cart_item_repo = _get_cart_item_repo(db)
    return cart_item_repo.get_by_cart_id(cart.id)

def update_cart_item_quantity(db: Session, user_id: int, product_id: int, quantity: int) -> CartItem | None:
    _get_user(db, user_id)
    cart = _get_cart(db, user_id)
    cart_item_repo = _get_cart_item_repo(db)
    cart_item = cart_item_repo.get_by_cart_and_product(cart.id, product_id)
    if not cart_item:
        return None
    cart_item.quantity = quantity
    return cart_item_repo.update(cart_item)