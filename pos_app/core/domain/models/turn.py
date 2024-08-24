import uuid
from datetime import datetime
from decimal import Decimal
from pos_app.core.domain.models.employee import Employee

class Turn:
    def __init__(self, turn_date: datetime):
        self.turn_id = uuid.uuid4()
        self.employees = {}
        self.turn_date = turn_date
        self.turn_end = None
        self.turn_status = ""
        self.total = Decimal(0)
        
    def to_dict(self) -> dict:
        return {
            "id": self.turn_id,
            "employees": {employee.id: employee.to_dict() for employee in self.employees},
            "date": self.date,
            "end": self.end,
            "status": self.status,
            "total": self.total
        }
        
    def add_employee(self, employee: Employee):
        self.employees[employee.__hash__()] = employee
        
    def remove_employee(self, employee: Employee):
        if employee.__hash__() in self.employees:
            del self.employees[employee.__hash__()]
        self.set_total()
        
    def add_service(self, service) -> None:
        self.turn_services.append(service)
    
    def add_product(self, product) -> None:
        self.turn_products.append(product)

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