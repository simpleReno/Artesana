import os
import datetime
import uuid
from typing import Any
from decimal import Decimal
from dotenv import load_dotenv
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, payment_order
load_dotenv()

class Payment(Base):
    __tablename__ = 'payments'

    id_ = Column("id", String, primary_key=True, unique=True, index=True, nullable=False)
    payment_type = Column("payment_type", String)
    payed = Column("payed", Float)
    date = Column("date", DateTime)
    orders = relationship('Order', secondary=payment_order, back_populates='payments')
    turn_id = Column("turn_id", String, ForeignKey('turns.id'), nullable=False)
    turn = relationship('Turn', back_populates='payments')
    employee_id = Column("employee_id", String, ForeignKey('employees.id'), nullable=False)
    employee = relationship('Employee', back_populates='payments')
    bill_id = Column("bill_id", String, ForeignKey('bills.id'), nullable=False)
    bill = relationship('Bill', back_populates='payments')
    bill_amount = Column("bill_amount", Float)
    bill_total = Column("bill_total", Float)
    
    def __init__(self, payment_type: str, orders: dict[str, dict], order_total: Decimal):
        self.id_ = uuid.uuid4().hex()
        self.type = payment_type
        self.payed = Decimal(0)
        self.date = datetime.datetime.now()
        self.orders = {order[id]: order for order in orders.items()}
        self.total = order_total
        self.date = datetime.datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self.id_,
            "type": self.type,
            "payed": self.payed,
            "orders": self.orders,
            "total": self.total,
            "date": self.date,
        }
    
    def get_products(self) -> dict:
        products = {}
        for order in self.orders.values():
            for product in order.products.values():
                products[product["id"]] = product
        return products
        
    def get_type(self) -> str:
        return self.type
    
    def set_type(self, payment_type: str) -> None:
        if payment_type not in os.getenv("PAYMENT_TYPES").split(","):
            raise ValueError("Invalid payment type")
        self.type = payment_type
        
    def get_total(self) -> Decimal:
        return self.total
        
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Payment):
            return self.id_ == other.id_
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.id_)
    
    def __repr__(self) -> str:
        return f"Payment(id={self.id_}, amount={self.amount}, date={self.date})"
    
    def __str__(self) -> str:
        return f"Payment {self.id_}"
