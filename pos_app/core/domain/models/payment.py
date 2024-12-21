from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid

class Payment(Base):
    """
    Represents a payment made for an order detail.

    Attributes:
        id (str): The unique identifier for the payment.
        order_detail_id (str): The ID of the associated order detail.
        amount_paid (float): The amount paid for the order detail.
        payment_date (datetime): The date and time when the payment was made.
    
    Relationships:
        order_detail (OrderDetail): The associated order detail object.

    """

    __tablename__ = "payments"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    order_detail_id = Column(String(36), ForeignKey("order_details.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)

    order_detail = relationship("OrderDetail", back_populates="payments")
    
    def to_dict(self):
        return {
            "id": self.id,
            "order_detail_id": self.order_detail_id,
            "amount_paid": self.amount_paid,
            "payment_date": self.payment_date,
        }
        
    def __repr__(self):
        return f"<Payment(amount_paid={self.amount_paid}, payment_date={self.payment_date})>"