from sqlalchemy import (
    Column, String, Float, Integer, ForeignKey, DateTime, Boolean
)
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid


class Customer(Base):
    """
    Represents a customer in the POS application.

    Attributes:
        id (str): The unique identifier for the customer.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        email (str): The email address of the customer.
        address (str): The address of the customer.
        discounts (float): The discounts applicable to the customer.
        table_id (str): The foreign key referencing the associated table.

    Relationships:
        table (Table): The table associated with the customer.
    """

    __tablename__ = "customers"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    address = Column(String(255))
    discounts = Column(Float, default=0.0)
    table_id = Column(String(36), ForeignKey("tables.id"))

    table = relationship("Table", back_populates="customers")
    
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
            "discounts": self.discounts,
            "table_id": self.table_id,
        }
    
    def __repr__(self):
        return f"<Customer(first_name='{self.first_name}', last_name='{self.last_name}')>"
