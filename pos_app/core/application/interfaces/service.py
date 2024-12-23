from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.table import Table
from pos_app.core.domain.models.payment import Payment


"""_summary_
    This module contains the interfaces for the services of the application.
"""

# The service interfaces define the methods that the service classes must implement to interact with the repository classes.
# The service classes are responsible for the business logic of the application. The service classes use the repository classes
# to interact with the database.
############################################################################################################
class ICustomerService(ABC):
    @abstractmethod
    def create_customer(self, customer: dict):
        pass
    
    @abstractmethod
    def update_customer(self, customer_id: str, customer: dict):
        pass
    
    @abstractmethod
    def get_customer(self, customer_id: str):
        pass
    
    @abstractmethod
    def get_all_customers(self):
        pass
    
    @abstractmethod
    def delete_customer(self, customer_id: str):
        pass
############################################################################################################
class IOrderService(ABC):
    @abstractmethod
    def create_order(self, order: Order) -> Order:
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
    
    @abstractmethod
    def get_total(self, order_id: str) -> Decimal:
        pass
    
############################################################################################################
class IProductService(ABC):
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
class ITableService(ABC):
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
class ICategoryService(ABC):
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
class IPaymentService(ABC):
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
