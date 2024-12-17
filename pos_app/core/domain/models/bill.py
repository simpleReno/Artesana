import uuid
from decimal import Decimal
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID  # Use this for PostgreSQL
from pos_app.core.domain.models.base import Base


class Bill(Base):
    __tablename__ = 'bills'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    total = Column(Float)
    date = Column(DateTime, default=func.now())
    orders = relationship('Order', back_populates='bills')
    table_id = Column(String, ForeignKey('tables.id'), nullable=False)
    table = relationship('Table', back_populates='orders')
    turn_id = Column(String, ForeignKey('turns.id'), nullable=False)
    turn = relationship('Turn', back_populates='bills')
    employee_id = Column(String, ForeignKey('employees.id'), nullable=False)
    employee = relationship('Employee', back_populates='bills')
    amount = Column("amount",Float)
    payments = relationship('Payment', back_populates='bills')
    
    def __int__(self, amount: Decimal, orders: dict[str, dict]) -> None:
        self.id_ = uuid.uuid4()
        self.total = Decimal(0)
        self.date = func.now()
        self.orders = {order['id']: order for order in orders}
        self.table_id = ""
        self.turn_id = ""
        self.employee_id = ""
        self.amount = amount
        self.payments = {}
          
    def to_dict(self) -> dict:
        return {
            "id": self.bill_id,
            "total": self.total,
            "date": self.date,
            "orders": {order['id']: order for order in self.orders.items()},
            "table_id": self.table_id,
            "turn_id": self.turn_id,
            "employee_id": self.employee_id,
            "amount": self.amount,
            "payments": {payment.id: payment.to_dict() for payment in self.payments}
        }
        
    def get_amount(self) -> float:
        return self.amount
    
    def set_amount(self, amount: float) -> None:
        self.amount = amount
        
    def add_order(self, order: dict) -> None:
        self.orders[order.__hash__()] = order
        self.set_total()
    
    def remove_order(self, order: dict) -> None:
        if order.__hash__() in self.orders:
            del self.orders[order.__hash__()]
        self.set_total()
        
    def set_total(self) -> None:
        self.total = Decimal(0)
        for order in self.orders:
            self.total += order.total    
        
    def get_total(self) -> float:
        return self.total

            
    def __eq__(self, other) -> bool:
        if not isinstance(other, Bill):
            return False
        return self.id_ == other.id_
    
    def __hash__(self) -> int:
        return hash(self.bill_id)
    
    def __repr__(self) -> str:
        return f"Bill(id={self.id_}, amount={self.amount}, total={self.total})"
    
    def __str__(self) -> str:
        return f"Bill {self.id_}  - {self.amount} - {self.total}"