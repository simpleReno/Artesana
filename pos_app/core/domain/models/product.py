from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid

class Product(Base):
    """
    Represents a product in the system.

    Attributes:
        id (str): The unique identifier of the product.
        product_name (str): The name of the product.
        category_id (str): The ID of the category to which the product belongs.
        price (float): The price of the product.
        description (str): The description of the product.
        stock (int): The current stock quantity of the product.
        
    Relationships:
        order_details (list): The list of order details associated with the product.
        category (Category): The category to which the product belongs.
    """

    __tablename__ = "products"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    product_name = Column(String(100), nullable=False)
    category_id = Column(String(36), ForeignKey("categories.id"), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255))
    stock = Column(Integer, default=0)

    order_details = relationship("OrderDetail", back_populates="product")
    category = relationship("Category", back_populates="products")
    
    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "category_id": self.category_id,
            "price": self.price,
            "description": self.description,
            "stock": self.stock,
        }
    
    def __repr__(self):
        return f"<Product(product_name='{self.product_name}', price={self.price})>"