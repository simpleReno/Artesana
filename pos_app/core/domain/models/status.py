import os
import datetime
from typing import Any
from dotenv import load_dotenv

load_dotenv()

class Status:
    def __init__(self):
        self.name = ""
        self.last_time_changed = None
        
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "last_time_changed": self.last_time_changed
        }
        
    def set_name(self, name: str) -> None:
        if name not in os.getenv("STATUS_TYPES").split(","):
            raise ValueError("Invalid status")
        self.name = name
        self.last_time_changed = datetime.datetime.now()
        
    def get_name(self) -> str:
        return self.name
    
    def get_last_time_changed(self) -> datetime.datetime:
        return self.last_time_changed
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Status):
            return self.name == other.name
        return NotImplemented
    
    def __repr__(self) -> str:
        return f"Status(name={self.name}, last_time_changed={self.last_time_changed})"
    
    def __str__(self) -> str:
        return f"Status {self.name}"