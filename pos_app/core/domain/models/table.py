import uuid
from decimal import Decimal
from typing import List
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from pos_app.core.domain.models.order import Order

class Table:
    __tablename__ = 'tables'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column("name",String, unique=True)
    seats = Column("seats", Integer)
    orders = relationship('Order', back_populates='tables')
    status = Column("status", String)
    total = Column("total", Float)
        
    def to_dict(self) -> dict:
        return {
            "id": self.id_,
            "number": self.number,
            "seats": self.seats,
            "orders": self.orders,
            "status": self.status,
            "total": float(self.total)
        }
        
    def clear_table(self) -> None:
        self.orders = {}
        self.total = Decimal(0)
        self.status = "open"
        
    def set_seats(self, seats: int) -> None:
        self.seats = seats
        
    def get_seats(self) -> int:
        return self.seats
    
    def get_orders(self) -> List[Order]:
        return self.orders
    
    def add_order(self, order: Order) -> None:
        self.orders[order.id] = order
    
    def remove_order(self, order: Order) -> None:
        if order.id in self.orders:
            del self.orders[order.id]
            
    def get_status(self) -> str:
        return self.status
    
    def set_status_busy(self) -> None:
        self.status = "busy"
        
    def set_status_open(self) -> None:
        self.status = "open"

    def set_total(self) -> None:
        self.total = sum([order.total for order in self.orders.values()])


    def __eq__(self, other) -> bool:
        if not isinstance(other, Table):
            return False
        return self.id_ == other.id_

    def __hash__(self) -> int:
        return hash(self.id_)

    def __repr__(self) -> str:
        return f"<Table(id={self.id_}, number={self.number},seats={self.seats},status={self.status},orders={len(self.orders)}, total={self.total})>"
    
    def __str__(self) -> str:
        return f"Table {self.id_}"