import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from pos_app.core.domain.models.base import Base, employee_role, role_turn


class Role(Base):
    
    __tablename__ = 'roles'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, unique=True)
    description = Column(String)
    employees = relationship('Employee', secondary=employee_role, back_populates='roles')
    turns = relationship('Turn', secondary=role_turn, back_populates='roles')

    def to_dict(self) -> dict:
        return {
            "id": self.id_,
            "name": self.name,
            "description": self.description,
            "employees": self.employees,
            "turns": self.turns
        }
        
    def get_id(self) -> int:
        return self.id_
    
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
    
    def add_employee(self, employee_id: str, employee_name: str) -> None:
        self.employees[employee_id] = employee_name
        
    def remove_employee(self, employee_id: str) -> None:
        if employee_id in self.employees:
            del self.employees[employee_id]
            
    def __eq__(self, other) -> bool:
        if not isinstance(other, Role):
            return False
        return self.id_ == other.id_
    
    def __hash__(self) -> int:
        return hash(self.id_)
    
    def __repr__(self) -> str:
        return f"Role(name={self.name}, description={self.description})"
    
    def __str__(self) -> str:
        return f"Role {self.name}"