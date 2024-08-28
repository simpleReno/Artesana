import uuid
from decimal import Decimal
from typing import List
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.payment import Payment


class Bill:
    def __int__(self, amount: Decimal, orders: List[Order]):
        self.id = uuid.uuid4()
        self.amount = amount
        self.orders = {order.__hash__(): order for order in orders}
        self.payments = {}
        self.total = Decimal(0)
        
    def to_dict(self) -> dict:
        return {
            "id": self.bill_id,
            "amount": self.amount,
            "orders": {order.id: order.to_dict() for order in self.orders},
            "payments": {payment.id: payment.to_dict() for payment in self.payments},
            "total": self.total
        }
        
    def get_amount(self) -> float:
        return self.amount
    
    def set_amount(self, amount: float) -> None:
        self.amount = amount
        
    def add_order(self, order: Order) -> None:
        self.orders[order.__hash__()] = order
        self.set_total()
    
    def remove_order(self, order: Order) -> None:
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
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.bill_id)
    
    def __repr__(self) -> str:
        return f"Bill(id={self.id}, amount={self.amount}, total={self.total})"
    
    def __str__(self) -> str:
        return f"Bill {self.id}  - {self.amount} - {self.total}"