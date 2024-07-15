# Description: Item model class.
from decimal import Decimal

class Item:
    def __init__(self, item_id: int, name: str, price: Decimal):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __eq__(self, other) -> bool:
        if not isinstance(other, Item):
            return False
        return self.name == other.name and self.price == other.price

    def __hash__(self) -> int:
        return hash((self.name, self.price))

    def __repr__(self) -> str:
        return f"Item(name={self.name}, price={self.price})"
    
    def __str__(self) -> str:
        return f"{self.name} - {self.price}"