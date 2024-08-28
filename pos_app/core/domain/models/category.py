import datetime
from pos_app.core.domain.models.product import Product


class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.product = {}
        self.last_time_added = datetime.datetime.now()

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "products": [product.to_dict() for product in self.product],
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
        
    def get_products(self) -> dict[Product]:
        return self.product
    
    def add_product(self, product: Product) -> None:
        self.product[product.__hash__()] = product
        
    def remove_product(self, product: Product) -> None:
        if product.__hash__() in self.product:
            del self.product[product.__hash__()]
            
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
        
