from sqlalchemy.orm import Session

from app.entities.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository

def create_user(db: Session, user: UserCreate) -> User:
    user_repo = UserRepository(db)
    db_user = user_repo.get_by_email(user.email)
    if db_user:
        raise ValueError("Email already registered")
    new_user = User(**user.dict())
    return user_repo.create(new_user)

def get_user_by_id(db: Session, user_id: int) -> User | None:
    user_repo = UserRepository(db)
    return user_repo.get_by_id(user_id)

def get_user_by_username(db: Session, username: str) -> User | None:
    user_repo = UserRepository(db)
    return user_repo.get_by_username(username)

def get_user_by_email(db: Session, email: str) -> User | None:
    user_repo = UserRepository(db)
    return user_repo.get_by_email(email)

def get_active_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    user_repo = UserRepository(db)
    return user_repo.get_active_users(skip, limit)