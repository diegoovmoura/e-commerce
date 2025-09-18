from typing import Type, TypeVar, Generic, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], db: Session):
        self.model = model
        self.db = db

    def create(self, obj: T) -> T:
        try:
            self.db.add(obj)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except SQLAlchemyError:
            self.db.rollback()
            raise

    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, obj: T) -> T:
        try:
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except SQLAlchemyError:
            self.db.rollback()
            raise

    def delete(self, obj: T) -> None:
        try:
            self.db.delete(obj)
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise

    def delete_by_id(self, id: int) -> bool:
        obj = self.get_by_id(id)
        if obj:
            self.delete(obj)
            return True
        return False

    def exists(self, id: int) -> bool:
        return self.db.query(self.model).filter(self.model.id == id).first() is not None

    def count(self) -> int:
        return self.db.query(self.model).count()