from fastapi import APIRouter, HTTPException, Depends
from app.entities.product import Product
from app.schemas.product_schema import ProductCreate, ProductOut
from app.utils.db import get_db
from sqlalchemy.orm import Session
from app.services.product_service import create_product, get_product_by_id, get_products

router = APIRouter()

@router.post("/", response_model=ProductOut)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return create_product(db, product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProductOut])
def read_products_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_products(db, skip, limit)

@router.get("/{product_id}", response_model=ProductOut)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product