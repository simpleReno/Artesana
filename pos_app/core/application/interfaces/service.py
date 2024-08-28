from abc import ABC, abstractmethod
from typing import List
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.table import Table
from pos_app.core.domain.models.employee import Employee
from pos_app.core.domain.models.turn import Turn
from pos_app.core.domain.models.payment import Payment


"""_summary_
    This module contains the interfaces for the services of the application.
"""

# The service interfaces define the methods that the service classes must implement to interact with the repository classes.
# The service classes are responsible for the business logic of the application. The service classes use the repository classes
# to interact with the database.

############################################################################################################
class OrderService(ABC):
    @abstractmethod
    def create_order(self, table_id: str, order: Order) -> Order:
        pass
    
    @abstractmethod
    def update_order(self, order_id: str, order: Order) -> Order:
        pass
    
    @abstractmethod
    def split_order(self, table_id: str, order_id: str, order: Order, selected_products: List[Product]) -> List[Order]:
        pass
    
    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        pass
    
    @abstractmethod
    def get_all_orders(self) -> List[Order]:
        pass
    
    @abstractmethod
    def delete_order(self, order_id: str) -> None:
        pass
    
    @abstractmethod
    def close_order(self, order_id: str) -> None:
        pass
    
    @abstractmethod
    def cancel_order(self, order_id: str) -> None:
        pass
    
    @abstractmethod
    def add_product(self, order_id: str, product: Product) -> Order:
        pass
    
    @abstractmethod
    def remove_product(self, order_id: str, product_id: str) -> Order:
        pass
    
    @abstractmethod
    def add_payment(self, order_id: str, payment: Payment) -> Order:
        pass
    
############################################################################################################
class ProductService(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass
    
    @abstractmethod
    def update_product(self, product_id: str, product: Product):
        pass
    
    @abstractmethod
    def get_product(self, product_id: str):
        pass
    
    @abstractmethod
    def get_all_products(self):
        pass
    
    @abstractmethod
    def delete_product(self, product_id: str):
        pass

############################################################################################################
class TableService(ABC):
    @abstractmethod
    def create_table(self, table: Table):
        pass
    
    @abstractmethod
    def update_table(self, table_id: str, table: Table):
        pass
    
    @abstractmethod
    def get_table(self, table_id: str):
        pass
    
    @abstractmethod
    def get_all_tables(self):
        pass
    
    @abstractmethod
    def delete_table(self, table_id: str):
        pass
############################################################################################################
class EmployeeService(ABC):
    @abstractmethod
    def create_employee(self, employee: Employee):
        pass
    
    @abstractmethod
    def update_employee(self, employee_id: str, employee: Employee):
        pass
    
    @abstractmethod
    def get_employee(self, employee_id: str):
        pass
    
    @abstractmethod
    def get_all_employees(self):
        pass
    
    @abstractmethod
    def delete_employee(self, employee_id: str):
        pass
############################################################################################################
class CategoryService(ABC):
    @abstractmethod
    def create_category(self, category: dict):
        pass
    
    @abstractmethod
    def update_category(self, category_id: str, category: dict):
        pass
    
    @abstractmethod
    def get_category(self, category_id: str):
        pass
    
    @abstractmethod
    def get_all_categories(self):
        pass
    
    @abstractmethod
    def delete_category(self, category_id: str):
        pass
############################################################################################################
class RoleService(ABC):
    @abstractmethod
    def create_role(self, role: dict):
        pass
    
    @abstractmethod
    def update_role(self, role_id: str, role: dict):
        pass
    
    @abstractmethod
    def get_role(self, role_id: str):
        pass
    
    @abstractmethod
    def get_all_roles(self):
        pass
    
    @abstractmethod
    def delete_role(self, role_id: str):
        pass
############################################################################################################
class TurnService(ABC):
    @abstractmethod
    def create_turn(self, turn: Turn):
        pass
    
    @abstractmethod
    def update_turn(self, turn_id: str, turn: Turn):
        pass
    
    @abstractmethod
    def get_turn(self, turn_id: str):
        pass
    
    @abstractmethod
    def get_all_turns(self):
        pass
    
    @abstractmethod
    def delete_turn(self, turn_id: str):
        pass
############################################################################################################
class PaymentService(ABC):
    @abstractmethod
    def create_payment(self, payment: Payment):
        pass
    
    @abstractmethod
    def update_payment(self, payment_id: str, payment: Payment):
        pass
    
    @abstractmethod
    def get_payment(self, payment_id: str):
        pass
    
    @abstractmethod
    def get_all_payments(self):
        pass
    
    @abstractmethod
    def delete_payment(self, payment_id: str):
        pass

############################################################################################################
