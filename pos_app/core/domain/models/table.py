from typing import List
from pos_app.core.domain.models.order import Order

class Table:
    def __init__(self, number: int):
        self.number = number
        self.seats = 0
        self.orders = 0
        
    def set_seats(self, seats: int) -> None:
        self.seats = seats
        
    def get_seats(self) -> int:
        return self.seats
    
    def get_orders(self) -> List[Order]:
        return self.orders
    
    def add_order(self, order: Order) -> None:
        self.orders.append(order)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Table):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"<Table {self.id}>"