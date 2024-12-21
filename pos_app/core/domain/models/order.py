from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid

class Order(Base):
    """
    Represents an order made by a customer in the POS system.

    Attributes:
        id (str): The unique identifier of the order.
        order_date (datetime): The date and time when the order was placed.
        delivery_id (str): The unique identifier of the delivery associated with the order.
        table_id (str): The unique identifier of the table where the order was placed.
        customer_id (str): The unique identifier of the customer who placed the order.
        total (float): The total amount of the order.
        
    Relationships:
        table (Table): The table associated with the order.
        customer (Customer): The customer who placed the order.
        order_details (list[OrderDetail]): The details of the order.

    Methods:
        is_fully_paid(): Checks if the order is fully paid.

    """

    __tablename__ = "orders"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    order_date = Column(DateTime, default=datetime.utcnow)
    delivery_id = Column(String(36), ForeignKey("deliveries.id"))
    table_id = Column(String(36), ForeignKey("tables.id"))
    customer_id = Column(String(36), ForeignKey("customers.id"))
    total = Column(Float, nullable=False)

    table = relationship("Table", back_populates="orders")
    customer = relationship("Customer")
    order_details = relationship("OrderDetail", back_populates="order")

    @property
    def is_fully_paid(self):
        """
        Checks if the order is fully paid.

        Returns:
            bool: True if all order details are paid, False otherwise.
        """
        return all(detail.paid for detail in self.order_details)