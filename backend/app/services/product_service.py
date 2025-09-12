from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
import app.repositories.product_repository as product_repo

def create_product(db: Session, product: ProductCreate) -> Product:
    if product.price <= 0:
        raise ValueError("Product price must be positive")
    if product.stock < 0:
        raise ValueError("Product stock cannot be negative")
    db_product = Product(**product.dict())
    return product_repo.create(db, db_product)

def get_product_by_id(db: Session, product_id: int) -> Product | None:
    return product_repo.get_by_id(db, product_id)

def get_products(db: Session, skip: int = 0, limit: int = 10) -> list[Product]:
    return product_repo.get_all(db, skip, limit)

def update_product(db: Session, product_id: int, product_update: ProductUpdate) -> Product | None:
    db_product = product_repo.get_by_id(db, product_id)
    if not db_product:
        return None
    if product_update.price is not None and product_update.price <= 0:
        raise ValueError("Product price must be positive")
    if product_update.stock is not None and product_update.stock < 0:
        raise ValueError("Product stock cannot be negative")
    for key, value in product_update.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    return product_repo.update(db, product_id, db_product)

def delete_product(db: Session, product_id: int) -> bool:
    db_product = product_repo.get_by_id(db, product_id)
    if not db_product:
        return False
    product_repo.delete(db, db_product)
    return True