from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import mapped_column
from pos_app.adapters.database.psql_adapter.connection import Base

employee_role = Table('employee_role', Base.metadata,
                        mapped_column('employee_id', String, ForeignKey('employees.id')),
                        mapped_column('role_id', String, ForeignKey('roles.id'))
                        )

employee_turn = Table('employee_turn', Base.metadata,
                        mapped_column('employee_id', String, ForeignKey('employees.id')),
                        mapped_column('turn_id', String, ForeignKey('turn.id'))
                        )
  
role_turn = Table('role_turn', Base.metadata,
                    mapped_column('role_id', String, ForeignKey('roles.id')),
                    mapped_column('turn_id', String, ForeignKey('turn.id'))
                    )

payment_order = Table('payment_order', Base.metadata,
                        mapped_column('payment_id', String, ForeignKey('payments.id')),
                        mapped_column('order_id', String, ForeignKey('orders.id'))
                        )

payment_employee = Table('payment_employee', Base.metadata,
                        mapped_column('payment_id', String, ForeignKey('payments.id')),
                        mapped_column('employee_id', String, ForeignKey('employees.id'))
                        )

payment_turn = Table('payment_turn', Base.metadata,
                        mapped_column('payment_id', String, ForeignKey('payments.id')),
                        mapped_column('turn_id', String, ForeignKey('turn.id'))
                        )
