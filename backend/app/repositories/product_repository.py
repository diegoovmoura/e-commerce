from sqlalchemy.orm import Session
from app.models.product import Product

def create(db: Session, product: Product) -> Product: 
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_by_id(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def get_all(db: Session, skip: int = 0, limit: int = 10) -> list[Product]:
    return db.query(Product).offset(skip).limit(limit).all()

def update(db: Session, product_id: int, product: Product) -> Product | None:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return None

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

def delete(db: Session, product_id: int) -> bool:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return False

    db.delete(db_product)
    db.commit()
    return True