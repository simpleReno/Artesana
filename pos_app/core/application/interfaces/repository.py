from abc import ABC, abstractmethod

"""_summary_
    This module contains the interfaces for the repository of the application.
"""

# The repository interfaces are similar to the service interfaces. The difference is that the repository interfaces are 
# responsible for the data access layer of the application. The repository interfaces define the methods that
# the repository classes must implement to interact with the database. 
############################################################################################################
class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def get(self, order_id):
        pass
    
    @abstractmethod
    def update(self, order_id, order):
        pass

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, order):
        pass
############################################################################################################
class ProductRepository(ABC):
    @abstractmethod
    def save(self, product):
        pass
    
    @abstractmethod
    def get(self, product_id):
        pass
    
    @abstractmethod
    def update(self, product_id, product):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, product):
        pass
############################################################################################################    
class TableRepository(ABC):
    @abstractmethod
    def save(self, table):
        pass
    
    @abstractmethod
    def get(self, table_id):
        pass
    
    @abstractmethod
    def update(self, table_id, table):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, table):
        pass
############################################################################################################
class CategoryRepository(ABC):
    @abstractmethod
    def save(self, category):
        pass
    
    @abstractmethod
    def get(self, category_id):
        pass
    
    @abstractmethod
    def update(self, category_id, category):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, category):
        pass
############################################################################################################
class EmployeeRepository(ABC):
    @abstractmethod
    def save(self, employee):
        pass
    
    @abstractmethod
    def get(self, employee_id):
        pass
    
    @abstractmethod
    def update(self, employee_id, employee):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, employee):
        pass
############################################################################################################
class RoleRepository(ABC):
    @abstractmethod
    def save(self, role):
        pass
    
    @abstractmethod
    def get(self, role_id):
        pass
    
    @abstractmethod
    def update(self, role_id, role):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, role):
        pass
############################################################################################################
class TurnRepository(ABC):
    @abstractmethod
    def save(self, turn):
        pass
    
    @abstractmethod
    def get(self, turn_id):
        pass
    
    @abstractmethod
    def update(self, turn_id, turn):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, turn):
        pass
############################################################################################################
class PaymentRepository(ABC):
    @abstractmethod
    def save(self, payment):
        pass
    
    @abstractmethod
    def get(self, payment_id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
