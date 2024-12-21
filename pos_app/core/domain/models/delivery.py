from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid

class Delivery(Base):
    """
    Represents a delivery in the system.

    Attributes:
        id (str): The unique identifier of the delivery.
        type (str): The type of the delivery.
        status (str): The status of the delivery.
        
    Relationships:
        orders (list): The orders associated with the delivery.
    """

    __tablename__ = "deliveries"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    type = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)

    orders = relationship("Order", back_populates="delivery")  
    
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "status": self.status,
        }
        
    def __repr__(self):
        return f"<Delivery(type='{self.type}', status='{self.status}')>"
