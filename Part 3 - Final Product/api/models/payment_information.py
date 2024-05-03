from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = 'payment_information'

    transaction_status = Column(String(100), default="Pending", nullable=False)
    payment_type = Column(String(100))
    card_information = Column(String(500), primary_key=True, nullable=False)
    promotion_code = Column(String(100))
    promotion_expiration = Column(DATETIME)
    order_id = Column(Integer, ForeignKey("orders.id"))

    order = relationship("Order", back_populates="payment_information")