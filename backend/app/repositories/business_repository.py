from sqlalchemy.orm import Session
from app.models.business import Business

def get_by_id(db: Session, business_id: int) -> Business | None:
    return db.query(Business).filter(Business.id == business_id).first()