from pos_app.core.application.interfaces.service import IOrderService

class OrderService(IOrderService):
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def create_order(self, order):
        return self.order_repository.save(order)

    def update_order(self, order_id, order):
        return self.order_repository.update(order_id, order)

    def split_order(self, table_id, order_id, order, selected_products):
        pass

    def get_order(self, order_id):
        return self.order_repository.get(order_id)

    def get_all_orders(self):
        return self.order_repository.get_all()

    def delete_order(self, order_id):
        return self.order_repository.delete(order_id)

    def close_order(self, order_id):
        pass

    def cancel_order(self, order_id):
        pass

    def add_product(self, order_id, product):
        pass

    def remove_product(self, order_id, product_id):
        pass

    def add_payment(self, order_id, payment):
        pass

    def get_total(self, order_id):
        pass