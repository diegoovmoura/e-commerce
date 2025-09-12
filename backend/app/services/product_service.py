from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate

def create_product(db: Session, product: ProductCreate) -> Product: 
    # Example business rule: price must be positive
    if product.price <= 0:
        raise ValueError("Product price must be positive")
    # Example business rule: stock must be non-negative
    if product.stock < 0:
        raise ValueError("Product stock cannot be negative")
    # Create and save product
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product_by_id(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10) -> list[Product]:
    return db.query(Product).offset(skip).limit(limit).all()