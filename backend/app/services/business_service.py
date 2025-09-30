from sqlalchemy.orm import Session
from typing import Optional, Dict, Any

from app.entities.business import Business
from app.repositories.business_repository import BusinessRepository
from app.schemas.business_schema import BusinessCreate, BusinessUpdate

class BusinessService:
    def __init__(self, db: Session):
        self.db = db
        self.business_repository = BusinessRepository(db)

    def create_business_from_schema(self, business_data: BusinessCreate) -> Business:
        if self.business_repository.exists_by_name(business_data.name):
            raise ValueError("Business with this name already exists")
        
        new_business = Business(
            name=business_data.name,
            contact_email=business_data.email,
            phone_number=business_data.phone,
            address=getattr(business_data, 'description', '')
        )
        return self.business_repository.create(new_business)

    def update_business_from_schema(self, business_id: int, business_update: BusinessUpdate) -> Optional[Business]:
        existing_business = self.business_repository.get_by_id(business_id)
        if not existing_business:
            return None
        
        update_data = {}
        if business_update.name is not None:
            update_data["name"] = business_update.name
        if business_update.email is not None:
            update_data["contact_email"] = business_update.email
        if business_update.phone is not None:
            update_data["phone_number"] = business_update.phone
        if business_update.description is not None:
            update_data["address"] = business_update.description
        
        if update_data:
            self.db.query(Business).filter(Business.id == business_id).update(update_data)
            self.db.commit()
            return self.business_repository.get_by_id(business_id)
        
        return existing_business

    def delete_business_by_id(self, business_id: int) -> bool:
        return self.business_repository.delete_by_id(business_id)

    def get_business(self, business_id: int) -> Optional[Business]:
        return self.business_repository.get_by_id(business_id)
    
    def get_by_name(self, name: str) -> Optional[Business]:
        return self.business_repository.get_by_name(name)
    
    def search_businesses(self, name: str, skip: int = 0, limit: int = 100) -> list[Business]:
        return self.business_repository.search_by_name(name, skip, limit)

    def delete_business(self, business_id: int) -> None:
        business = self.business_repository.get_by_id(business_id)
        if business:
            self.business_repository.delete(business)
