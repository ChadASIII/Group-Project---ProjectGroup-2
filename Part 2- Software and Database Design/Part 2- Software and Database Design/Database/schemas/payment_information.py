from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .orders import Order

class PaymentInformationBase(BaseModel):
    transaction_status: str
    payment_type = str
    card_information = str
    promotion_code = Optional[str] = None
    promotion_expiration = Optional[datetime] = None

class PaymentInformationCreate(PaymentInformationBase):
    pass


class PaymentInformationUpdate(BaseModel):
    transaction_status: Optional[str] = None
    payment_type = Optional[str] = None
    card_information = Optional[str] = None
    promotion_code = Optional[str] = None
    promotion_expiration = Optional[datetime] = None


class PaymentInformation(PaymentInformationBase):

    transaction_status: Optional[str] = None
    order: Optional[Order] = None

    class ConfigDict:
        from_attributes = True