from sqlalchemy.orm import Session
from app.models.business import Business

def create(db: Session, business: Business) -> Business:
    db.add(business)
    db.commit()
    db.refresh(business)
    return business

def get_by_id(db: Session, business_id: int) -> Business | None:
    return db.query(Business).filter(Business.id == business_id).first()

def get_all(db: Session) -> list[Business]:
    return db.query(Business).all()

def update(db: Session, business: Business) -> Business:
    db.merge(business)
    db.commit()
    return business

def delete(db: Session, business: Business) -> None:
    db.delete(business)
    db.commit()