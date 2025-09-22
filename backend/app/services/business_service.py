from sqlalchemy.orm import Session

from app.entities.business import Business
from app.repositories.business_repository import BusinessRepository

class BusinessService:
    def __init__(self, db: Session):
        self.db = db
        self.business_repository = BusinessRepository(db)

    def create_business(self, business: Business) -> Business:
        return self.business_repository.create(business)

    def get_business(self, business_id: int) -> Business:
        return self.business_repository.get(business_id)
    
    def get_by_name(self, name: str) -> Business:
        return self.business_repository.get_by_name(name)
    
    def search_businesses(self, name: str, skip: int = 0, limit: int = 100) -> list[Business]:
        return self.business_repository.search_by_name(name, skip, limit)

    def update_business(self, business: Business) -> Business:
        return self.business_repository.update(business)

    def delete_business(self, business_id: int) -> None:
        self.business_repository.delete(business_id)
