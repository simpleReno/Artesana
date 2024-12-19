import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import Column, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID  # Use this for PostgreSQL
from pos_app.core.domain.models.employee import Employee
from pos_app.core.domain.models.role import Role
from pos_app.core.domain.models.payment import Payment
from pos_app.core.domain.models.base import Base

class Turn(Base):
    __tablename__ = 'turns'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    start_time = Column("start_time", DateTime)
    end_time = Column("end_time", DateTime)
    status = Column("status", String)
    employees = relationship('Employee', back_populates='turns')
    roles = relationship('Role', back_populates='turns')
    payments = relationship('Payment', back_populates='turns')
    total = Column("total", Float)

    def to_dict(self) -> dict:
        return {
            "id": self.turn_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "status": self.turn_status,
            "employees": {employee.id: employee.to_dict() for employee in self.employees},
            "roles": {role.id: role.to_dict() for role in self.roles},
            "payments": {payment.id: payment.to_dict() for payment in self.payments},
            "total": self.total
        }
        
    def add_employee(self, employee: Employee):
        self.employees[employee.__hash__()] = employee
        
    def remove_employee(self, employee: Employee):
        if employee.__hash__() in self.employees:
            del self.employees[employee.__hash__()]
        self.set_total()
        
    def add_role(self, role: Role):
        self.roles[role.__hash__()] = role
        
    def remove_role(self, role: Role):
        if role.__hash__() in self.roles:
            del self.roles[role.__hash__()]
        self.set_total()
        
    def add_payment(self, payment: Payment):
        self.payments[payment.__hash__()] = payment
        self.set_total()
        
    def remove_payment(self, payment: Payment):
        if payment.__hash__() in self.payments:
            del self.payments[payment.__hash__()]
        self.set_total()
        
    def set_total(self):
        self.total = Decimal(0)
        for payment in self.payments:
            self.total += payment.amount
            
    def get_start_time(self) -> datetime:
        return self.start_time
    
    def set_start_time(self, start_time: datetime) -> None:
        self.start_time = start_time
        
    def get_end_time(self) -> datetime:
        return self.end_time
    
    def set_end_time(self, end_time: datetime) -> None:
        self.end_time = end_time
        
    def get_status(self) -> str:
        return self.turn_status
    
    def set_status(self, status: str) -> None:
        self.turn_status = status
        
    def get_employees(self) -> dict[str, str]:
        return self.employees
    
    def get_roles(self) -> dict[str, str]:
        return self.roles
    
    def get_payments(self) -> dict[str, str]:
        return self.payments
    
    def get_total(self) -> Decimal:
        return self.total
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Turn):
            return False
        return self.turn_id == other.turn_id

    def __hash__(self) -> int:
        return hash(self.turn_id)
    
    def __str__(self):
        return f'{self.turn_id} - {self.turn_date} - {self.turn_start} - {self.turn_end} - {self.turn_status}'
    
    def __repr__(self) -> str:
        return f"Turn(turn_id={self.turn_id}, turn_date={self.turn_date}, turn_start={self.turn_start}, turn_end={self.turn_end}, turn_status={self.turn_status})"