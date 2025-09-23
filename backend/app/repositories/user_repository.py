from typing import Optional, List
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserUpdate
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

    def update_current_user(self, user: User, update_data: UserUpdate):
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(user, key, value)
        
        self.db.commit()
        self.db.refresh(user)
        return user

    def change_password(self, user: User, new_hashed_password: str) -> User:
        user.hashed_password = new_hashed_password
        self.db.commit()
        self.db.refresh(user)
        return user