import uuid
from decimal import Decimal
from typing import List
from pos_app.core.domain.models.order import Order

class Table:
    def __init__(self, number: str):
        self.id = uuid.uuid4()
        self.number = number
        self.seats = 0
        self.orders = {}
        self.status = "open"
        self.total = Decimal(0)
        
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "number": self.number,
            "seats": self.seats,
            "orders": {order.id: order.to_dict() for order in self.orders},
            "status": self.status,
            "total": self.total
        }
        
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
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"<Table(id={self.id}, 
                        number={self.number},
                        seats={self.seats},
                        status={self.status},
                        orders={len(self.orders)},
                        total={self.total})>"
    
    def __str__(self) -> str:
        return f"Table {self.id}"