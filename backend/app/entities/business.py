from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.db import Base

class Business(Base):
    __tablename__ = 'businesses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    address = Column(String)

    products = relationship("Product", back_populates="business")