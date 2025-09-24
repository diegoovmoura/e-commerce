from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('businesses.id'), index=True)
    product_name = Column(String, index=True)
    product_description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    image_url = Column(String)
    
    business = relationship("Business", back_populates="products")