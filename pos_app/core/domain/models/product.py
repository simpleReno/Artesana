import datetime
import uuid
from typing import Any

class Product:
    def __init__(self, name: str, price: float, amount: int):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.amount = 0
        self.last_time_added = datetime.datetime
        
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "amount": self.amount,
            "last_time_added": self.last_time_added
        }
        
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_price(self) -> float:
        return self.price
    
    def set_price(self, price: float) -> None:
        self.price = price
    
    def get_amount(self) -> int:
        return self.amount
    
    def set_amount(self, amount: int) -> None:
        self.amount = amount
        
    def get_last_time_added(self) -> datetime.datetime:
        return self.date_to_added
    
    def set_last_time_added(self, date_time: datetime.datetime) -> None:
        self.last_time_added = date_time
        
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Product):
            return self.id == other.id
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name}, price={self.price}, amount={self.amount})"
    
    def __str__(self) -> str:
        return f"Product {self.name}"
    
        