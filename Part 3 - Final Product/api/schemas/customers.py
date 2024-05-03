from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order

class CustomerBase(BaseModel):
    customer_name: str
    customer_email: str
    customer_phone_number: str
    customer_address: str
    customer_rating: Optional[int] = None
    customer_review: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone_number: Optional[str] = None
    customer_address: Optional[str] = None
    customer_rating: Optional[int] = None
    customer_review: Optional[str] = None


class Customer(CustomerBase):
    customer_email: str

    class ConfigDict:
        from_attributes = True

