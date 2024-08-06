from abc import ABC, abstractmethod

"""_summary_
    This module contains the interfaces for the ports of the application.
"""

# Repository interfaces
class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass

    @abstractmethod
    def get(self, order_id):
        pass

    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, order):
        pass

# Service interfaces
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, payment):
        pass
    
class OrderService(ABC):
    @abstractmethod
    def create_order(self, order):
        pass
    
    @abstractmethod
    def get_order(self, order_id):
        pass
    
    @abstractmethod
    def get_all_orders(self):
        pass
    
    @abstractmethod
    def delete_order(self, order):
        pass