import os 
import uuid
import datetime
from decimal import Decimal
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID  # Use this for PostgreSQL
from pos_app.core.domain.models.base import Base, employee_role, employee_turn, payment_employee

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    pin = Column(String, unique=True, nullable=False)
    roles = relationship('Role', secondary=employee_role, back_populates='employees')
    turns = relationship('Turn', secondary=employee_turn, back_populates='employees')
    payments = relationship('Payment', secondary=payment_employee, back_populates='employees')
    start_date = Column(DateTime)
    stop_date = Column(DateTime)
        
    def to_dict(self) -> dict:
        return {
            "id": self.id_,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "pin": self.pin,
            "roles": self.roles,
            "turns": self.turns,
            "payments": {payment.id: payment for payment in self.payments},
            "start_date": self.start_date,
            "stop_date": self.stop_date,
            "last_time_added": self.last_time_added
        }
    
    def get_id(self) -> str:
        return self.id_
    
    def get_first_name(self) -> str:
        return self.first_name
    
    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name
        
    def get_last_name(self) -> str:
        return self.last_name
    
    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name
        
    def get_email(self) -> str:
        return self.email
    
    def set_email(self, email: str) -> None:
        self.email = email
        
    def get_pin(self) -> str:
        return self.pin
    
    def set_pin(self, pin: str) -> None:
        self.pin = pin
        
    def get_roles(self) -> dict[str, str]:
        return self.roles
    
    def add_role(self, role_id: str, role_name: str) -> None:
        self.roles[role_id] = role_name
        
    def remove_role(self, role_id: str) -> None:
        if role_id in self.roles:
            del self.roles[role_id]
            
    def get_turns(self) -> dict[str, str]:
        return self.turns
    
    def add_turn(self, turn_id: str, turn_name: str) -> None:
        self.turns[turn_id] = turn_name
        
    def remove_turn(self, turn_id: str) -> None:
        if turn_id in self.turns:
            del self.turns[turn_id]
            
    def get_payments(self) -> dict[str, dict]:
        return {payment.id: payment for payment in self.payments}
    
    def add_payment(self, payment: dict) -> None:
        self.payments[payment.id] = payment
        
    def remove_payment(self, payment_id: str) -> None:
        if payment_id in self.payments:
            del self.payments[payment_id]
            
    def get_start_date(self) -> datetime.datetime:
        return self.start_date
    
    def set_start_date(self, start_date: datetime.datetime) -> None:
        self.start_date = start_date
        
    def get_stop_date(self) -> datetime.datetime:
        return self.stop_date
    
    def set_stop_date(self, stop_date: datetime.datetime) -> None:
        self.stop_date = stop_date
        
    def get_last_time_added(self) -> datetime.datetime:
        return self.last_time_added
    
    def set_last_time_added(self, last_time_added: datetime.datetime) -> None:
        self.last_time_added = last_time_added
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Employee):
            return False
        return self.id_ == other.id_
    
    def __hash__(self) -> int:
        return hash(self.id_)
    
    def __repr__(self) -> str:
        return f"Employee(id={self.id_}, first_name={self.first_name},last_name={self.last_name},roles={len(self.roles)},turns={len(self.turns)},payments={len(self.payments)},start_date={self.start_date},stop_date={self.stop_date},last_time_added={self.last_time_added})"
                        
    def __str__(self) -> str:
        return f"Employee {self.first_name} {self.last_name}"