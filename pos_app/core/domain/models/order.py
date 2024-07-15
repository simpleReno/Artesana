# Description: Order model class
from decimal import Decimal
from typing import Any, List
from pos_app.core.domain.models.item import Item

class Order:
    def __init__(self, order_id, order_items: List[Item]):
        self.order_id = order_id
        self.order_items = order_items

    def total(self) -> Decimal:
        return sum([item.total() for item in self.order_items], Decimal(0))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Order):
            return False
        return self.order_id == other.order_id

    def __hash__(self) -> int:
        return hash(self.order_id)

    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id}, order_items={self.order_items})"

    def __str__(self) -> str:
        return f"Order {self.order_id}"