from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_name = Column(String(100))
    customer_email = Column(String(300), primary_key=True, index=True)
    customer_phone_number = Column(String(100))
    customer_address = Column(String(300))
    customer_rating = Column(Integer)
    customer_review = Column(String(500))
