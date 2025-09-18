from typing import List, Optional
from sqlalchemy.orm import Session
from app.entities.cart import Cart
from app.repositories.base_repository import BaseRepository

class CartRepository(BaseRepository[Cart]):
    def __init__(self, db: Session):
        super().__init__(Cart, db)
    
    def get_by_user_id(self, user_id: int) -> Optional[Cart]:
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()
    
    def create_for_user(self, user_id: int) -> Cart:
        cart = Cart(user_id=user_id)
        return self.create(cart)
    
    def get_or_create_for_user(self, user_id: int) -> Cart:
        cart = self.get_by_user_id(user_id)
        if not cart:
            cart = self.create_for_user(user_id)
        return cart