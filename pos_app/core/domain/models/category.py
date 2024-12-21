from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from pos_app.core.domain.models.base import Base, generate_uuid

class Category(Base):
    """
    Represents a category in the application.

    Attributes:
        id (str): The unique identifier of the category.
        category_name (str): The name of the category.
        category_type (str): The type of the category.
        parent_id (str): The ID of the parent category, if any.
        
    Relationships:
        subcategories (list): The list of subcategories under this category.
        products (list): The list of products belonging to this category.
    """

    __tablename__ = "categories"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    category_name = Column(String(100), nullable=False)
    category_type = Column(String(50))
    parent_id = Column(String(36), ForeignKey("categories.id"))

    subcategories = relationship("Category", backref="parent", remote_side=[id])
    products = relationship("Product", back_populates="category")
    
    def to_dict(self):
        return {
            "id": self.id,
            "category_name": self.category_name,
            "category_type": self.category_type,
            "parent_id": self.parent_id,
        }
        
    def __repr__(self):
        return f"<Category(category_name='{self.category_name}')>"


