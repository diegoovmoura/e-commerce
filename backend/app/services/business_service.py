from typing import Optional, List
import re
from sqlalchemy.orm import Session

from app.entities.business import Business
from app.repositories.business_repository import BusinessRepository
from app.schemas.business_schema import BusinessCreate, BusinessUpdate


class BusinessDomainException(Exception):
    pass


class BusinessService:
    def __init__(self, db: Session):
        self.business_repository = BusinessRepository(db)

    def create_business(self, business_data: BusinessCreate) -> Business:
        if self._is_business_name_taken(business_data.name):
            raise BusinessDomainException(f"Business with name '{business_data.name}' already exists")
        
        self._validate_business_data(business_data)
        formatted_business = self._create_business_entity(business_data)
        return self.business_repository.create(formatted_business)

    def update_business(self, business_id: int, business_update: BusinessUpdate) -> Optional[Business]:
        existing_business = self.business_repository.get_by_id(business_id)
        if not existing_business:
            raise BusinessDomainException(f"Business with ID {business_id} not found")
        
        if business_update.name and business_update.name != existing_business.name:
            if self._is_business_name_taken(business_update.name):
                raise BusinessDomainException(f"Business name '{business_update.name}' is already taken")
        
        return self._apply_business_updates(existing_business, business_update)

    def delete_business(self, business_id: int) -> bool:
        existing_business = self.business_repository.get_by_id(business_id)
        if not existing_business:
            return False
            
        if self._can_business_be_deleted(existing_business):
            return self.business_repository.delete_by_id(business_id)
        else:
            raise BusinessDomainException("Cannot delete business with active products or orders")

    def get_business_by_id(self, business_id: int) -> Optional[Business]:
        return self.business_repository.get_by_id(business_id)
    
    def get_business_by_name(self, name: str) -> Optional[Business]:
        return self.business_repository.get_by_name(name)
    
    def search_businesses(self, name_query: str, skip: int = 0, limit: int = 100) -> List[Business]:
        if limit > 100:
            limit = 100
        return self.business_repository.search_by_name(name_query, skip, limit)

    def get_all_businesses(self, skip: int = 0, limit: int = 100) -> List[Business]:
        if limit > 100:
            limit = 100
        return self.business_repository.get_all(skip, limit)

    def _is_business_name_taken(self, name: str) -> bool:
        return self.business_repository.exists_by_name(name)

    def _validate_business_data(self, business_data: BusinessCreate) -> None:
        if not business_data.name or len(business_data.name.strip()) < 2:
            raise BusinessDomainException("Business name must be at least 2 characters long")
        
        if len(business_data.name) > 255:
            raise BusinessDomainException("Business name cannot exceed 255 characters")
        
        if business_data.contact_email and not self._is_valid_business_email(business_data.contact_email):
            raise BusinessDomainException("Invalid business email format")
        
        if business_data.phone_number and not self._is_valid_phone_number(business_data.phone_number):
            raise BusinessDomainException("Invalid phone number format")

    def _create_business_entity(self, business_data: BusinessCreate) -> Business:
        return Business(
            name=self._format_business_name(business_data.name),
            contact_email=self._format_email(business_data.contact_email),
            phone_number=self._format_phone_number(business_data.phone_number),
            address=self._format_address(business_data.address)
        )

    def _apply_business_updates(self, business: Business, updates: BusinessUpdate) -> Optional[Business]:
        update_data = {}
        
        if updates.name is not None:
            formatted_name = self._format_business_name(updates.name)
            update_data['name'] = formatted_name
        
        if updates.contact_email is not None:
            if updates.contact_email and not self._is_valid_business_email(updates.contact_email):
                raise BusinessDomainException("Invalid business email format")
            update_data['contact_email'] = self._format_email(updates.contact_email)
        
        if updates.phone_number is not None:
            if updates.phone_number and not self._is_valid_phone_number(updates.phone_number):
                raise BusinessDomainException("Invalid phone number format")
            update_data['phone_number'] = self._format_phone_number(updates.phone_number)
        
        if updates.address is not None:
            update_data['address'] = self._format_address(updates.address)
        
        if update_data:
            return self.business_repository.update_entity(business, update_data)
        
        return business

    def _can_business_be_deleted(self, business: Business) -> bool:
        return True

    def _format_business_name(self, name: str) -> str:
        if not name:
            return name
        return name.strip().title()

    def _format_email(self, email: Optional[str]) -> Optional[str]:
        if not email:
            return email
        return email.strip().lower()

    def _format_phone_number(self, phone: Optional[str]) -> Optional[str]:
        if not phone:
            return phone
        digits_only = re.sub(r'[^\d]', '', phone)
        return digits_only

    def _format_address(self, address: Optional[str]) -> Optional[str]:
        if not address:
            return address
        return address.strip()

    def _is_valid_business_email(self, email: str) -> bool:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None

    def _is_valid_phone_number(self, phone: str) -> bool:
        digits_only = re.sub(r'[^\d]', '', phone)
        return 7 <= len(digits_only) <= 15
