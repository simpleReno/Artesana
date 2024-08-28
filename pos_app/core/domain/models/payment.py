import os
import datetime
import uuid
from typing import Any
from decimal import Decimal
from dotenv import load_dotenv
from pos_app.core.domain.models.order import Order

load_dotenv()

class Payment:
    def __init__(self, payment_type: str, orders: dict[Order]):
        self.id = uuid.uuid4()
        self.type = payment_type
        self.amount_payed = Decimal(0)
        self.orders = orders
        self.total = sum([order.total for order in orders], Decimal(0))
        self.date = datetime.datetime.now()

        # Add products from each order to the products dictionary
        for order in orders.values():
            for product in order.products.values():
                self.products[product.id] = product
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type,
            "amount_payed": self.amount_payed,
            "orders": {order.id: order.to_dict() for order in self.orders},
            "total": self.total,
            "date": self.date,
        }
    
    def get_products(self) -> dict:
        products = {}
        for order in self.orders.values():
            for product in order.products.values():
                products[product.id] = product
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
            return self.id == other.id
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __repr__(self) -> str:
        return f"Payment(id={self.id}, amount={self.amount}, date={self.date})"
    
    def __str__(self) -> str:
        return f"Payment {self.id}"
