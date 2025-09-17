from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.entities.user import User
from app.utils.db import Base

class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)

    user = relationship("User", back_populates="cart")
    items = relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")
    total_price = Column(Integer, default=0)