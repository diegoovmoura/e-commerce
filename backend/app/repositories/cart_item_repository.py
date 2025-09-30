from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.cart_item import CartItem
from app.repositories.base_repository import BaseRepository

class CartItemRepository(BaseRepository[CartItem]):
    def __init__(self, db: Session):
        super().__init__(CartItem, db)
    
    def get_by_cart_id(self, cart_id: int) -> List[CartItem]:
        return self.db.query(CartItem).filter(CartItem.cart_id == cart_id).all()
    
    def get_by_cart_and_product(self, cart_id: int, product_id: int) -> Optional[CartItem]:
        return self.db.query(CartItem).filter(
            CartItem.cart_id == cart_id,
            CartItem.product_id == product_id
        ).first()
    
    def delete_by_cart_id(self, cart_id: int) -> None:
        self.db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
        self.db.commit()
    
    def update_quantity(self, cart_item_id: int, quantity: int) -> Optional[CartItem]:
        cart_item = self.get_by_id(cart_item_id)
        if cart_item:
            self.db.query(CartItem).filter(CartItem.id == cart_item_id).update({"quantity": quantity})
            self.db.commit()
            self.db.refresh(cart_item)
        return cart_item