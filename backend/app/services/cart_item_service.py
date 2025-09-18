from sqlalchemy import Session

from app.entities.cart_item import CartItem
from app.repositories.cart_item_repository import CartItemRepository

class CartItemService:
    def __init__(self, db: Session):
        self.repository = CartItemRepository(db)
    
    def create_cart_item(self, cart_item_data: dict) -> CartItem:
        return self.repository.create(cart_item_data)
    
    def get_cart_item_by_id(self, item_id: int) -> CartItem:
        return self.repository.get_by_id(item_id)
    
    def get_cart_items_by_cart_id(self, cart_id: int) -> list[CartItem]:
        return self.repository.get_by_cart_id(cart_id)
    
    def update_cart_item(self, item_id: int, update_data: dict) -> CartItem:
        return self.repository.update(item_id, update_data)
    
    def delete_cart_item(self, item_id: int) -> bool:
        return self.repository.delete(item_id)
    
    def get_all_cart_items(self) -> list[CartItem]:
        return self.repository.get_all()