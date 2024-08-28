import uuid
from pos_app.core.domain.models.employee import Employee
from pos_app.core.domain.models.turn import Turn

class Role:
    def __int__ (self, name: str, description: str):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.employees = {}
        self.turns = {}

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "employees": {employee.id: employee.to_dict() for employee in self.employees},
            "turns": {turn.id: turn.to_dict() for turn in self.turns}
        }
        
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description: str) -> None:
        self.description = description
        
    def get_employees(self) -> dict[str, str]:
        return self.employees
    
    def add_employee(self, employee: Employee) -> None:
        self.employees[employee.__hash__] = employee
        
    def remove_employee(self, employee: Employee) -> None:
        if employee.id in self.employees:
            del self.employees[employee.__hash__]
            
    def get_turns(self) -> dict[str, str]:
        return self.turns
    
    def add_turn(self, turn: Turn) -> None:
        self.turns[turn.__hash__] = turn
        
    def remove_turn(self, turn: Turn) -> None:
        if turn.id in self.turns:
            del self.turns[turn.__hash__]
            
    def __eq__(self, other) -> bool:
        if not isinstance(other, Role):
            return False
        return self.id == other.id
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __repr__(self) -> str:
        return f"Role(name={self.name}, description={self.description})"
    
    def __str__(self) -> str:
        return f"Role {self.name}"