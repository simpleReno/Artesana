from sqlalchemy.orm import Session
from pos_app.core.domain.models.order import Order
from pos_app.core.application.interfaces.repository import IOrderRepository




class OrderRepository(IOrderRepository):
    def __init__(self, session: Session):
        self.session = session
    def save(self, order: Order) -> Order:
        try:
            order_entity = Order(
                id = order.id,
                name = order.name,
                type = order.type,
                products = order.products,
                payments = order.payments,
                table = order.table,
                status = order.status,
                total = order.total
            )
            self.session.add(order_entity)
            self.session.commit()
            self.session.refresh(order_entity)
            return order_entity
        except Exception as e:
            raise e
        finally:
            self.session.close()

    def get(self, order_id: str):
        pass
    
    def update(self, order_id: str, order: Order):
        pass

    def get_all(self):
        pass
    
    def delete(self, order_id: str):
        pass