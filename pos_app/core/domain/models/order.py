import os
import uuid
from decimal import Decimal
from typing import Any
from dotenv import load_dotenv
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.status import Status

load_dotenv()

class Order:
    def __init__(self, order_products: dict[Product]):
        self.order_id = uuid.uuid4()
        self.order_type = ""
        self.order_products = order_products
        self.status = Status("open")
        self.payment = None
        self.total = 0

    def to_dict(self) -> dict:
            return {
                "order_id": self.order_id,
                "order_products": [product.to_dict() for product in self.order_products],
                "status": self.status,
                "payment": self.payment,
                "table": self.table,
                "total": self.total
            }
            
    def get_order_type(self) -> str:
        return self.order_type

    def set_order_type(self, order_type: str) -> None:
        if order_type not in os.getenv("ORDER_TYPES").split(","):
            raise ValueError("Invalid order type")
        self.order_type = order_type

    def add_product(self, product: Product) -> None:
        self.order_products.append(product)
        self.total = self.total()
        
    def remove_product(self, product: Product) -> None:
        self.order_products.remove(product)
        self.total = self.total()
        
    def get_status(self) -> str:
        return self.status
        
    def set_status(self, status: str) -> None:
        self.status = Status(status)
        
    def get_payment(self) -> str:
        return self.payment
        
    def set_payment(self, payment: str) -> None:
        self.payment = payment
        
    def get_table(self) -> str:
        return self.table
    
    def set_table(self, table: str) -> None:
        self.table = table
    
    def get_total(self) -> Decimal:
        return self.total
    
    def set_total(self) -> None:
        self.total = sum([item.total() for item in self.order_products], Decimal(0))
        
    
    

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Order):   
            return self.order_id == other.order_id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.order_id)

    def __repr__(self) -> str:
        return f"Order(order_id={self.order_id}, order_products={self.order_products})"

    def __str__(self) -> str:
        return f"Order {self.order_id}"