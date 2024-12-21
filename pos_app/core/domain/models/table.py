from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid


class Table(Base):
    """
    The Table class represents a table in a restaurant's POS system.

    Attributes:
        id (str): The unique identifier of the table.
        table_type (str): The type of the table (e.g., "indoor", "outdoor").
        total (float): The total amount of the table's orders.
        
    Relationships:
        customers (relationship): The customers associated with the table.
        orders (relationship): The orders placed at the table.
    """

    __tablename__ = "tables"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    table_type = Column(String(50))
    total = Column(Float, default=0.0)

    customers = relationship("Customer", back_populates="table")
    orders = relationship("Order", back_populates="table")
    
    def to_dict(self):
        return {
            "id": self.id,
            "table_type": self.table_type,
            "total": self.total,
        }
        
    def __repr__(self):
        return f"<Table(table_type='{self.table_type}')>"
