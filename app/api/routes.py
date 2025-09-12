from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductOut
from app.utils.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = next(get_db())):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products/", response_model=list[ProductOut])
def read_products(skip: int = 0, limit: int = 10, db: Session = next(get_db())):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@router.get("/products/{product_id}", response_model=ProductOut)
def read_product(product_id: int, db: Session = next(get_db())):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product