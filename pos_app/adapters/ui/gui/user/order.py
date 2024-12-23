from pos_app.core.application.interfaces.user import IOrderUser

class OrderUser(IOrderUser):
    def __init__(self, order_service):
        self.order_service = order_service
        
    def create_order(self, order):
        return self.order_service.create_order(order)
    
    def update_order(self, order_id, order):
        return self.order_service.update_order(order_id, order)
    
    def split_order(self, table_id, order_id, order, selected_products):
        return self.order_service.split_order(table_id, order_id, order, selected_products)
    
    def get_order(self, order_id):
        return self.order_service.get_order(order_id)
    
    def get_all_orders(self):
        return self.order_service.get_all_orders()