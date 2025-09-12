from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"<Vendor(name={self.name}, contact_email={self.contact_email})>"