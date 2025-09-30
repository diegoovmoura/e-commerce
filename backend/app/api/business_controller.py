from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.schemas.business_schema import Business, BusinessCreate, BusinessUpdate
from app.schemas.product_schema import Product
from app.services.business_service import BusinessService
from app.auth.dependencies import get_current_active_user
from app.entities.user import User
from app.utils.db import get_db

router = APIRouter(prefix="/businesses")

@router.get("/", response_model=List[Business])
def get_businesses(
    skip: int = Query(0, ge=0, description="Number of businesses to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of businesses to return"),
    db: Session = Depends(get_db)
):
    business_service = BusinessService(db)
    return business_service.search_businesses("", skip=skip, limit=limit)

@router.get("/{business_id}", response_model=Business)
def get_business(
    business_id: int,
    db: Session = Depends(get_db)
):
    business_service = BusinessService(db)
    business = business_service.get_business(business_id)
    if not business:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Business not found"
        )
    return business

@router.get("/{business_id}/products", response_model=List[Product])
def get_business_products(
    business_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Get business products functionality not yet implemented"
    )

@router.post("/", response_model=Business, status_code=status.HTTP_201_CREATED)
def create_business(
    business_data: BusinessCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    try:
        business_service = BusinessService(db)
        return business_service.create_business_from_schema(business_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{business_id}", response_model=Business)
def update_business(
    business_id: int,
    business_update: BusinessUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    try:
        business_service = BusinessService(db)
        updated_business = business_service.update_business_from_schema(business_id, business_update)
        
        if not updated_business:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Business not found"
            )
        
        return updated_business
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{business_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_business(
    business_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    try:
        business_service = BusinessService(db)
        success = business_service.delete_business_by_id(business_id)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Business not found"
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )