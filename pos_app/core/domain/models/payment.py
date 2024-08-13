import os
import datetime
import uuid
from typing import Any
from dotenv import load_dotenv

load_dotenv()

class Payment:
    def __init__(self):
        self.payment_id = uuid.uuid4()
        self.payment_amount = 0
        self.payment_type = ""
        self.payment_date = datetime.datetime.now()
        
    def set_payment_amount(self, payment_amount: float) -> None:
        self.payment_amount = payment_amount
        
    def get_payment_amount(self) -> float:
        return self.payment_amount
    
    def set_payment_type(self, payment_type: str) -> None:
        if payment_type not in os.getenv("PAYMENT_TYPES").split(","):
            raise ValueError("Invalid payment type")
        self.payment_type = payment_type
    
    def get_payment_date(self) -> datetime.datetime:
        return self.payment_date
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Payment):
            return self.payment_id == other.payment_id
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.payment_id)
    
    def __repr__(self) -> str:
        return f"Payment(payment_id={self.payment_id}, payment_amount={self.payment_amount}, payment_date={self.payment_date})"
    
    def __str__(self) -> str:
        return f"Payment {self.payment_id}"
