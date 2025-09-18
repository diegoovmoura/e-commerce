from typing import Optional, List
from sqlalchemy.orm import Session
from app.entities.business import Business
from app.repositories.base_repository import BaseRepository

class BusinessRepository(BaseRepository[Business]):
    def __init__(self, db: Session):
        super().__init__(Business, db)
    
    def get_by_name(self, name: str) -> Optional[Business]:
        return self.db.query(self.model).filter(self.model.name == name).first()
    
    def search_by_name(self, name: str, skip: int = 0, limit: int = 100) -> List[Business]:
        return (self.db.query(self.model)
                .filter(self.model.name.ilike(f"%{name}%"))
                .offset(skip)
                .limit(limit)
                .all())
    
    def exists_by_name(self, name: str) -> bool:
        return self.db.query(self.model).filter(self.model.name == name).first() is not None
