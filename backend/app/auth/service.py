from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

from app.auth.utils import verify_password, get_password_hash, create_access_token
from app.repositories.user_repository import UserRepository

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY environment variable is not set")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(db, username: str, password: str):
    user_repo = UserRepository(db)
    user = user_repo.get_by_username(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def change_password_service(db, user_id: int, old_password: str, new_password: str):
    user_repo = UserRepository(db)
    user = user_repo.get_by_id(user_id)
    
    if not user:
        raise ValueError("User not found")
    
    if not verify_password(old_password, user.hashed_password):
        raise ValueError("Invalid current password")
    
    if len(new_password) < 6:
        raise ValueError("New password must be at least 6 characters long")
    
    if old_password == new_password:
        raise ValueError("New password must be different from current password")
    
    new_hashed_password = get_password_hash(new_password)
    return user_repo.change_password(user, new_hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, str(SECRET_KEY), algorithm=str(ALGORITHM))
    return encoded_jwt