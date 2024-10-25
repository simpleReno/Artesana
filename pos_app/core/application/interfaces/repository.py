from abc import ABC, abstractmethod
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.table import Table
from pos_app.core.domain.models.turn import Turn
from pos_app.core.domain.models.payment import Payment
from pos_app.core.domain.models.employee import Employee


"""_summary_
    This module contains the interfaces for the repository of the application.
"""

# The repository interfaces are similar to the service interfaces. The difference is that the repository interfaces are 
# responsible for the data access layer of the application. The repository interfaces define the methods that
# the repository classes must implement to interact with the database. 
############################################################################################################
class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def get(self, order_id: str):
        pass
    
    @abstractmethod
    def update(self, order_id: str, order: Order):
        pass

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, order_id: str):
        pass
############################################################################################################
class IProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product):
        pass
    
    @abstractmethod
    def get(self, product_id: str):
        pass
    
    @abstractmethod
    def update(self, product_id: str, product: Product):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, product_id: str):
        pass
############################################################################################################    
class ITableRepository(ABC):
    @abstractmethod
    def save(self, table: Table):
        pass
    
    @abstractmethod
    def get(self, table_id: str):
        pass
    
    @abstractmethod
    def update(self, table_id: str, table: Table):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, table_id: str):
        pass
############################################################################################################
class ICategoryRepository(ABC):
    @abstractmethod
    def save(self, category: dict):
        pass
    
    @abstractmethod
    def get(self, category_id: str):
        pass
    
    @abstractmethod
    def update(self, category_id: str, category: dict):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, category: dict):
        pass
############################################################################################################
class IEmployeeRepository(ABC):
    @abstractmethod
    def save(self, employee: Employee):
        pass
    
    @abstractmethod
    def get(self, employee_id: str):
        pass
    
    @abstractmethod
    def update(self, employee_id: str, employee: Employee):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, employee_id: str):
        pass
############################################################################################################
class IRoleRepository(ABC):
    @abstractmethod
    def save(self, role: dict):
        pass
    
    @abstractmethod
    def get(self, role_id: str):
        pass
    
    @abstractmethod
    def update(self, role_id, role: dict):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, role_id: str):
        pass
############################################################################################################
class ITurnRepository(ABC):
    @abstractmethod
    def save(self, turn: Turn):
        pass
    
    @abstractmethod
    def get(self, turn_id: str):
        pass
    
    @abstractmethod
    def update(self, turn_id, turn: Turn):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, turn_id: str):
        pass
############################################################################################################
class IPaymentRepository(ABC):
    @abstractmethod
    def save(self, payment: Payment):
        pass
    
    @abstractmethod
    def get(self, payment_id: str):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
