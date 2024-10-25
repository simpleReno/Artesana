from pos_app.core.application.interfaces.repository import IOrderRepository
from pos_app.core.application.interfaces.service import IOrderService
from decimal import Decimal
from typing import List
from pos_app.core.domain.models.order import Order
from pos_app.core.domain.models.product import Product
from pos_app.core.domain.models.payment import Payment

class OrderService(IOrderService):
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository
        
    def create_order(self, order: Order) -> Order:
        return self.order_repository.save(order)
    
    def update_order(self, order_id: str, order: Order) -> Order:
        pass
    
    def split_order(self, table_id: str, order_id: str, order: Order, selected_products: List[Product]) -> List[Order]:
        pass
    
    def get_order(self, order_id: str) -> Order:
        pass
    
    def get_all_orders(self) -> List[Order]:
        pass
    
    def delete_order(self, order_id: str) -> None:
        pass
    
    def close_order(self, order_id: str) -> None:
        pass
    
    def cancel_order(self, order_id: str) -> None:
        pass
    
    def add_product(self, order_id: str, product: Product) -> Order:
        pass
    
    def remove_product(self, order_id: str, product_id: str) -> Order:
        pass
    
    def add_payment(self, order_id: str, payment: Payment) -> Order:
        pass
    
    def get_total(self, order_id: str) -> Decimal:
        pass