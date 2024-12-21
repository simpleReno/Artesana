from sqlalchemy import Column, String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid

class OrderDetail(Base):
    """
    Represents the details of an order in the system.

    Attributes:
        id (str): The unique identifier of the order detail.
        order_id (str): The ID of the order that this detail belongs to.
        product_id (str): The ID of the product associated with this detail.
        amount (int): The quantity of the product in the order.
        subtotal (float): The subtotal cost of the product in the order.
        paid (bool): Indicates whether the product has been paid for or not.

    Relationships:
        order (Order): The order that this detail belongs to.
        product (Product): The product associated with this detail.
        payments (List[Payment]): The payments made for this order detail.
    """

    __tablename__ = "order_details"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    order_id = Column(String(36), ForeignKey("orders.id"), nullable=False)
    product_id = Column(String(36), ForeignKey("products.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)
    paid = Column(Boolean, default=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")
    payments = relationship("Payment", back_populates="order_detail")
    
    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "subtotal": self.subtotal,
            "paid": self.paid,
        }
    
    def __repr__(self):
        return f"<OrderDetail(product_id='{self.product_id}', amount={self.amount})>"