from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base

class OrderProduct(Base):
    __tablename__ = 'order_product'

    order_id = Column("order_id", String, ForeignKey('orders.id'), primary_key=True)
    product_id = Column("product_id", String, ForeignKey('products.id'), primary_key=True)
    quantity = Column("quantity", Integer, nullable=False)
    price_at_order = Column("price_at_order", Float, ForeignKey('products.price'), nullable=False)  # Store price at time of order
    discount = Column("discount", Float)  # Optional discount for each product

    # Relationships
    order = relationship('Order', back_populates='products')
    product = relationship('Product', back_populates='orders')
        
    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "price_at_order": self.price_at_order,
            "discount": self.discount
        }
        
    def get_order_id(self) -> str:
        return self.order_id
    
    def get_product_id(self) -> str:
        return self.product_id
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity
        
    def get_price_at_order(self) -> float:
        return self.price_at_order
    
    def set_price_at_order(self, price_at_order: float) -> None:
        self.price_at_order = price_at_order
        
    def get_discount(self) -> float:
        return self.discount
    
    def set_discount(self, discount: float) -> None:
        self.discount = discount
    
    def get_order_id(self) -> str:
        return self.order_id