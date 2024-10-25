from sqlalchemy import Column, String, Table, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

employee_role = Table('employee_role', Base.metadata,
                        Column('employee_id', String(), ForeignKey('employees.id'), nullable=False),
                        Column('role_id', String(), ForeignKey('roles.id'), nullable=False)
                        )

employee_turn = Table('employee_turn', Base.metadata,
                        Column('employee_id', String(), ForeignKey('employees.id'), nullable=False),
                        Column('turn_id', String(), ForeignKey('turns.id'), nullable=False)
                        )
  
role_turn = Table('role_turn', Base.metadata,
                    Column('role_id', String(), ForeignKey('roles.id'), nullable=False),
                    Column('turn_id', String(), ForeignKey('turns.id'), nullable=False)
                    )

payment_order = Table('payment_order', Base.metadata,
                        Column('payment_id', String(), ForeignKey('payments.id'), nullable=False),
                        Column('order_id', String(), ForeignKey('orders.id'), nullable=False)
                        )

payment_employee = Table('payment_employee', Base.metadata,
                        Column('payment_id', String(), ForeignKey('payments.id'), nullable=False),
                        Column('employee_id', String(), ForeignKey('employees.id'), nullable=False)
                        )

payment_turn = Table('payment_turn', Base.metadata,
                        Column('payment_id', String(), ForeignKey('payments.id'), nullable=False),
                        Column('turn_id', String(), ForeignKey('turns.id'), nullable=False)
                        )