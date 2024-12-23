from abc import ABC, abstractmethod
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.table import Table
from pos_app.core.domain.models.payment import Payment


"""_summary_
    This module contains the interfaces for the repository of the application.
"""

# The repository interfaces are similar to the service interfaces. The difference is that the repository interfaces are 
# responsible for the data access layer of the application. The repository interfaces define the methods that
# the repository classes must implement to interact with the database. 
############################################################################################################
class ICustomerRepository(ABC):
    @abstractmethod
    def save(self, customer: dict):
        pass
    
    @abstractmethod
    def get(self, customer_id: str):
        pass
    
    @abstractmethod
    def update(self, customer_id: str, customer: dict):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, customer_id: str):
        pass
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
    
