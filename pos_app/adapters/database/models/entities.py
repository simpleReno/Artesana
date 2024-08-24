from typing import List, Optional
from sqlalchemy import String, ForeignKey, Column, DateTime, Float, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pos_app.adapters.database.psql_adapter.connection import Base, engine
from pos_app.adapters.database.models.associations import employee_role, employee_turn, role_turn, payment_order, payment_employee, payment_turn



class TableEntity(Base):
    __tablename__ = 'tables'
    
    id: Mapped[str] = mapped_column(primary_key= True, unique= True, index=True, nullable=False)
    number: Mapped[int] = mapped_column(unique= True, nullable= False, index= True)
    seats: Mapped[int] = mapped_column(Optional[int])
    status: Mapped[str] = mapped_column(index= True)
    
    orders: Mapped[List["OrderEntity"]] = relationship(back_populates='TableEntity')

class OrderEntity(Base):
    __tablename__ = 'orders'

    id: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True, nullable=False)
    products: Mapped[List["ProductEntity"]] = relationship(back_populates= 'OrderEntity')
    payments: Mapped[List["PaymentEntity"]] = relationship(secondary=payment_order, back_populates= 'OrderEntity')
    
    table_id: Mapped[str] = mapped_column(ForeignKey('tables.id'), nullable=False)
    table: Mapped[TableEntity] = relationship(back_populates= 'OrderEntity')
    
    status: Mapped[str]
    total: Mapped[float] 

class CategoryEntity(Base):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True, nullable=False)
    product: Mapped[list["ProductEntity"]] = relationship(back_populates= 'CategoryEntity')
    description: Mapped[str]
    
class ProductEntity(Base):
    __tablename__ = 'products'

    id: Mapped[str] = mapped_column(primary_key=True, unique= True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[Float] = mapped_column()
    description: Mapped[str] = mapped_column()
    category_id: Mapped[str] = mapped_column(ForeignKey('categories.id'), nullable=False)
    category: Mapped[CategoryEntity] = relationship(back_populates='ProductEntity')
    
class EmployeeEntity(Base):
    __tablename__ = 'employees'

    id: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True, nullable=False)
    first_name: Mapped[str] 
    last_name: Mapped[str] 
    email: Mapped[Optional[str]] = mapped_column(unique=True)
    pin: Mapped[str] = mapped_column(unique=True, nullable=False)
    roles: Mapped[List["RoleEntity"]] = relationship(secondary=employee_role, back_populates = 'EmployeeEntity')
    turns: Mapped[List["TurnEntity"]] = relationship(secondary=employee_turn, back_populates = 'EmployeeEntity')
    payments: Mapped[List["PaymentEntity"]] = relationship(secondary=payment_employee, back_populates = 'EmployeeEntity')
    start_date: Mapped[DateTime]
    stop_date: Mapped[DateTime]
    
class RoleEntity(Base):
    __tablename__ = 'roles'

    id: Mapped[str] = Column(String, primary_key=True, unique=True, index=True, nullable=False)
    name: Mapped[str] = Column(String, unique=True)
    description: Mapped[str] = Column(String)
    employees: Mapped[List["EmployeeEntity"]] = relationship(secondary=employee_role, back_populates = 'RoleEntity')
    turns: Mapped[List ["TurnEntity"]] = relationship(secondary=role_turn, back_populates = 'RoleEntity')
    
class TurnEntity(Base):
    __tablename__ = 'turns'

    id: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True, nullable=False)
    start_time: Mapped[DateTime]
    end_time: Mapped[DateTime] 
    employees: Mapped[List["EmployeeEntity"]] = relationship(secondary=employee_turn, back_populates = 'TurnEntity')
    roles: Mapped[List["RoleEntity"]] = relationship(secondary=role_turn, back_populates = 'TurnEntity')
    payments: Mapped[List["PaymentEntity"]] = relationship(secondary=payment_turn, back_populates = 'TurnEntity')
    
class PaymentEntity(Base):
    __tablename__ = 'payments'

    id: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True, nullable=False)
    payment_type: Mapped[str]
    total: Mapped[Float]
    percentage: Mapped[Float]
    date: Mapped[DateTime] = mapped_column(default=func.now())
    orders: Mapped[list["OrderEntity"]] = relationship(secondary=payment_order, back_populates= 'PaymentEntity')
    turn_id: Mapped[str] = mapped_column(ForeignKey('turns.id'), nullable=False)
    turn: Mapped[TurnEntity] = relationship(back_populates= 'PaymentEntity')
    employee_id: Mapped[str] = mapped_column(ForeignKey('employees.id'), nullable=False)
    employee: Mapped[EmployeeEntity] = relationship(back_populates= 'PaymentEntity')

 
Base.metadata.create_all(bind=engine)