from typing import Optional, List
from sqlalchemy.orm import Session
from app.entities.user import User
from app.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)
    
    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.query(self.model).filter(self.model.username == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(self.model).filter(self.model.email == email).first()
    
    def exists_by_username(self, username: str) -> bool:
        return self.db.query(self.model).filter(self.model.username == username).first() is not None
    
    def exists_by_email(self, email: str) -> bool:
        return self.db.query(self.model).filter(self.model.email == email).first() is not None
    
    def get_active_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return (self.db.query(self.model)
                .filter(self.model.is_active == True)
                .offset(skip)
                .limit(limit)
                .all())

