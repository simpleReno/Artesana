from sqlalchemy import Column, String, Table, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())