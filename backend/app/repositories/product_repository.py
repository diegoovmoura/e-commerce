from sqlalchemy.orm import Session
from typing import Optional, List
from app.entities.product import Product
from app.repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository[Product]):
    def __init__(self, db: Session):
        super().__init__(Product, db)
    
    def get_by_business_id(self, business_id: int, skip: int = 0, limit: int = 100) -> List[Product]:
        return (self.db.query(self.model)
                .filter(self.model.business_id == business_id)
                .offset(skip)
                .limit(limit)
                .all())
    
    def search_by_name(self, name: str, skip: int = 0, limit: int = 100) -> List[Product]:
        return (self.db.query(self.model)
                .filter(self.model.name.ilike(f"%{name}%"))
                .offset(skip)
                .limit(limit)
                .all())
    
    def get_low_stock_products(self, threshold: int = 5) -> List[Product]:
        return (self.db.query(self.model)
                .filter(self.model.stock <= threshold)
                .all())

# Backward compatibility functions (to be deprecated)
