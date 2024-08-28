import os
import uuid
from decimal import Decimal
from typing import Any
from dotenv import load_dotenv
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.status import Status
from pos_app.core.domain.models.payment import Payment

load_dotenv()

class Order:
    def __init__(self, products: dict[Product]):
        self.id = uuid.uuid4()
        self.name = ""
        self.type = ""
        self.products = products
        self.status = Status("open")
        self.payments = []
        self.table = ""
        self.total = Decimal(0)

    def to_dict(self) -> dict:
            return {
                "id": self.order_id,
                "name": self.name,
                "type": self.order_type,
                "products": {product.id: product.to_dict() for product in self.products},
                "status": self.status,
                "payment": self.payment,
                "table": self.table,
                "total": self.total
            }
            
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
        
    def set_payment(self, payment: str) -> None:
        self.payments.append(Payment(payment))
    
    def get_total(self) -> Decimal:
        return self.total
    
    def set_total(self) -> None:
        self.total = sum([item.total() for item in self.products], Decimal(0))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Order):   
            return self.id == other.id
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.order_id)

    def __repr__(self) -> str:
        return f"Order(id={self.id}, products={self.products})"

    def __str__(self) -> str:
        return f"Order {self.id}"