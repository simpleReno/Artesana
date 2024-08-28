import uuid
from datetime import datetime

class User:
    def __init__(self, first_name: str, last_name: str, email: str, username: str, password: str):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pin = ""
        self.username = username
        self.password = password
        self.last_time_added = datetime.now()
        
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "pin": self.pin,
            "username": self.username,
            "last_time_added": self.last_time_added
        }
        
    def change_first_name(self, new_first_name: str):
        self.first_name = new_first_name
        self.last_time_added = datetime.now()
        
    def change_last_name(self, new_last_name: str):
        self.last_name = new_last_name
        self.last_time_added = datetime.now()
        
    def change_username(self, new_username: str):
        self.username = new_username
        self.last_time_added = datetime.now()
        
    def change_email(self, new_email: str):
        self.email = new_email
        self.last_time_added = datetime.now()    
        
    def change_password(self, new_password: str):
        self.password = new_password
        self.last_time_added = datetime.now()
    
    def add_pin(self, pin: str):
        self.pin = pin
        self.last_time_added = datetime.now()
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self.id == other.id
    
    