from sqlalchemy import Column, String, Table, Integer, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base, relationship
import uuid

metadata = MetaData()
Base = declarative_base(metadata=metadata)

def generate_uuid():
    return str(uuid.uuid4())