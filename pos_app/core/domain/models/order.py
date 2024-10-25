import os
import uuid
from decimal import Decimal
from typing import Any
from dotenv import load_dotenv
from sqlalchemy import Column, String, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.status import Status
from pos_app.core.domain.models.base import Base, payment_order
load_dotenv()

class Order(Base):
    __tablename__ = 'orders'

    id_ = Column("id", String, primary_key=True, unique=True, index=True, nullable=False)
    name = Column("name", String)
    type = Column("type", String)
    products = relationship('OrderProduct', back_populates='orders')
    payments = relationship('Payment',secondary=payment_order, back_populates='orders')
    table_id = Column("table_id", String, ForeignKey('tables.id'), nullable=False)
    table = relationship('Table', back_populates='orders')
    status = Column("status", Enum)
    total = Column("total", Float)
    
    def __init__(self, type: str, products: dict[str, dict], table_id: str, status: Status = Status("open"), name: str = ""):
        self.id_ = uuid.uuid4()
        self.name = name
        self.type = type
        self.products = products
        self.status = status
        self.payments = {}
        self.table_id = table_id
        self.total = float(Decimal(0))

    def to_dict(self) -> dict:
            return {
                "id": self.id_,
                "name": self.name,
                "type": self.order_type,
                "products": self.products,
                "status": self.status,
                "payments": self.payments,
                "table_id": self.table_id,
                "total": self.total
            }
            
    def get_id(self) -> str:
        return self.id_
            
    def get_type(self) -> str:
        return self.order_type

    def set_type(self, order_type: str) -> None:
        if order_type not in os.getenv("ORDER_TYPES").split(","):
            raise ValueError("Invalid order type")
        self.order_type = order_type

    def add_product(self, product: Product) -> None:
        self.products[product.__hash__()] = product
        self.set_total()
        
    def remove_product(self, product: Product) -> None:
        if product.__hash__() in self.products:
            del self.products[product.__hash__()]
        self.set_total()
        
    def get_status(self) -> str:
        return self.status
        
    def set_status(self, status: str) -> None:
        self.status = Status(status)
        
    def get_payment(self) -> str:
        return self.payments
        
    def set_payment(self, payment_id: str) -> None:
        self.payments = payment_id
    
    def get_total(self) -> Decimal:
        return self.total
    
    def set_total(self) -> None:
        self.total = sum([item.total() for item in self.products], Decimal(0))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Order):   
            return self.id_ == other.id_
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.id_)

    def __repr__(self) -> str:
        return f"Order(id={self.id_}, products={self.products})"

    def __str__(self) -> str:
        return f"Order {self.id_}"