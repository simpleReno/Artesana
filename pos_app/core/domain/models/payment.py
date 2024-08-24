import os
import datetime
import uuid
from typing import Any
from dotenv import load_dotenv

load_dotenv()

class Payment:
    def __init__(self):
        self.id = uuid.uuid4()
        self.amount = 0
        self.payment_type = ""
        self.date = datetime.datetime.now()
        
    def to_dict(self) -> dict:  
        return {
            "id": self.id,
            "amount": self.amount,
            "payment_type": self.payment_type,
            "date": self.date
        }
        
    def set_payment_amount(self, amount: float) -> None:
        self.amount = amount
        
    def get_payment_amount(self) -> float:
        return self.amount
    
    def set_payment_type(self, payment_type: str) -> None:
        if payment_type not in os.getenv("PAYMENT_TYPES").split(","):
            raise ValueError("Invalid payment type")
        self.payment_type = payment_type
    
    def get_payment_date(self) -> datetime.datetime:
        return self.date
    
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
