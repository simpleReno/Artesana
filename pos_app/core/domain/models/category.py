import uuid
import datetime
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID  # Use this for PostgreSQL
from pos_app.core.domain.models.base import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, unique=True)
    parent_id = Column(String, ForeignKey('categories.id_'), nullable=True)
    description = Column(String)
    
    subcategories = relationship("Categories",
        backref="parent",
        remote_side=[id],
        cascade="all, delete-orphan",
    )
    
    products = relationship("Product", back_populates="category")

    def to_dict(self) -> dict:
        return {
            "id": self.id_,
            "name": self.name,
            "description": self.description,
            "products": {product[id]:product for product in self.products},
            "subcategories": {category[id]:category for category in self.subcategories},
            "last_time_added": self.last_time_added
        }
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def get_description(self) -> str:
        return self.description
    
    def set_description(self, description: str) -> None:
        self.description = description
        
    def get_products(self) -> dict[str, dict]:
        return self.products
    
    def add_product(self, product: dict) -> None:
        self.products[product.id] = product
        
    def get_subcategories(self) -> dict[str, dict]:
        return self.subcategories
    
    def add_subcategory(self, category: dict) -> None:
        self.subcategories[category.id] = category
        
    def remove_subcategory(self, category: dict) -> None:
        if category.id in self.subcategories:
            del self.subcategories[category.id]
        
    def remove_product(self, product: dict) -> None:
        if product.id in self.products:
            del self.products[product.id]
            
    def get_last_time_added(self) -> datetime.datetime:
        return self.last_time_added
    
    def set_last_time_added(self, date_time: datetime.datetime) -> None:
        self.last_time_added = date_time
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Category):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __repr__(self) -> str:
        return f"Category(name={self.name}, description={self.description})"
    
    def __str__(self) -> str:
        return f"Category {self.name}"
        
