from abc import ABC, abstractmethod
from typing import List

"""_summary_
    This module contains the interfaces for the services of the application.
"""

# The service interfaces define the methods that the service classes must implement to interact with the repository classes.
# The service classes are responsible for the business logic of the application. The service classes use the repository classes
# to interact with the database.

############################################################################################################
class OrderService(ABC):
    @abstractmethod
    def create_order(self, order: dict):
        pass
    
    @abstractmethod
    def edit_order(self, order_id: str, order: dict):
        pass
    
    @abstractmethod
    def get_order(self, order_id: str):
        pass
    
    @abstractmethod
    def get_all_orders(self):
        pass
    
    @abstractmethod
    def delete_order(self, order_id: str):
        pass
############################################################################################################
class ProductService(ABC):
    @abstractmethod
    def create_product(self, product: dict):
        pass
    
    @abstractmethod
    def update_product(self, product_id: str, product: dict):
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
    def create_table(self, table: dict):
        pass
    
    @abstractmethod
    def update_table(self, table_id: str, table: dict):
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
    def create_employee(self, employee: dict):
        pass
    
    @abstractmethod
    def update_employee(self, employee_id: str, employee: dict):
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

