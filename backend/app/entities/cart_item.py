from sqlalchemy import Column, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.utils.db import Base

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Numeric(10, 2), nullable=False)  # Price per unit at time of adding
    
    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")
    
    @hybrid_property
    def subtotal(self):
        """Calculate subtotal as price * quantity"""
        return self.price * self.quantity
