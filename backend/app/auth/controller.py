from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.services.user_service import create_user
from app.auth.service import authenticate_user, create_access_token
import app.schemas.user_schema as schema
from app.auth.schemas import Token
from app.utils.db import get_db

router = APIRouter()

@router.post("/register", response_model=schema.User)
def register(user_data: schema.UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schema.UserProfile)
def get_current_user_profile(current_user: str = Depends(authenticate_user)):
    return current_user

@router.post("/me", response_model=schema.UserUpdate)
def update_current_user_profile(
    user_update: schema.UserUpdate,
    current_user: schema.User = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    user_repo = UserRepository(db)
    user = authenticate_user(db, current_user.username, current_user.password)
    return user_repo.update_current_user(user, user_update)

@router.post("/change-password", response_model=schema.PasswordChange)
def change_password(
    password_change: schema.PasswordChange,
    current_user: schema.User = Depends(authenticate_user),
    db: Session = Depends(get_db)
):
    try:
        from app.auth.service import change_password_service
        change_password_service(db, current_user.id, password_change.old_password, password_change.new_password)
        return {"message": "Password changed successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )