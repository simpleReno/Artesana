import datetime
import datetime
import uuid
from typing import Any
from decimal import Decimal
from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID  # Use this for PostgreSQL
from pos_app.core.domain.models.base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column("name", String, unique=True)
    amount = Column("amount", Integer)
    price = Column("price", Float)
    description = Column("description", String)
    last_time_added = Column("last_time_added", DateTime, default=datetime.datetime.now())
    category_id = Column("category_id", String, ForeignKey('categories.id_'), nullable=False)
    
    category = relationship('Category', back_populates='products')
    orders = relationship('OrderProduct', back_populates='product')
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "amount": self.amount,
            "last_time_added": self.last_time_added,
            "category": self.category
        }
        
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_price(self) -> float:
        return self.price
    
    def set_price(self, price: float) -> None:
        self.price = price
        
    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description: str) -> None:
        self.description = description
    
    def get_amount(self) -> int:
        return self.amount
    
    def set_amount(self, amount: int) -> None:
        self.amount = amount
        
    def get_last_time_added(self) -> datetime.datetime:
        return self.date_to_added
    
    def set_last_time_added(self, date_time: datetime.datetime) -> None:
        self.last_time_added = date_time
        
    def get_category(self) -> str:
        return self.category
    
    def set_category(self, category: str) -> None:
        self.category = category
        
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Product):
            return self.id_ == other.id_
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name}, price={self.price}, amount={self.amount})"
    
    def __str__(self) -> str:
        return f"Product {self.name}"
    
        