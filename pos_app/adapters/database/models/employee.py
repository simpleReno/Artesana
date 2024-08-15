import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine

class EmployeeEntity(Base):
    __tablename__ = 'Employees'

    id = Column(Integer, primary_key=True, unique=True)
    products_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Products', back_populates= 'categories')
    description = Column(String)
 
    
Base.metadata.create_all(bind=engine)