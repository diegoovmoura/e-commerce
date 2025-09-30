from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.schemas.product_schema import Product, ProductCreate, ProductUpdate
from app.services.product_service import (
    create_product as create_product_service,
    get_product_by_id as get_product_by_id_service,
    get_products as get_products_service,
    update_product as update_product_service,
    delete_product as delete_product_service
)
from app.auth.dependencies import get_current_active_user
from app.entities.user import User
from app.utils.db import get_db

router = APIRouter(prefix="/products")

@router.get("/", response_model=List[Product])
def get_products(
    skip: int = Query(0, ge=0, description="Number of products to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of products to return"),
    db: Session = Depends(get_db)
):
    return get_products_service(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=Product)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product_by_id_service(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    try:
        return create_product_service(db, product_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    try:
        product = update_product_service(db, product_id, product_update)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        return product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    success = delete_product_service(db, product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )