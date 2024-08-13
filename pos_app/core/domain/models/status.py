import os
import datetime
from typing import Any
from dotenv import load_dotenv

load_dotenv()

class Status:
    def __init__(self):
        self.status_name = ""
        self.last_time_changed = None
        
    def set_status_name(self, status_name: str) -> None:
        if status_name not in os.getenv("STATUS_TYPES").split(","):
            raise ValueError("Invalid status")
        self.status_name = status_name
        self.last_time_changed = datetime.datetime.now()
        
    def get_status_name(self) -> str:
        return self.status_name
    
    def get_last_time_changed(self) -> datetime.datetime:
        return self.last_time_changed
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Status):
            return self.status_name == other.status_name
        return NotImplemented
    
    def __repr__(self) -> str:
        return f"Status(status_name={self.status_name}, last_time_changed={self.last_time_changed})"
    
    def __str__(self) -> str:
        return f"Status {self.status_name}"