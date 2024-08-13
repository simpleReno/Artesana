import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine

class order(Base):
    __tablename__ = 'Orders'

    order_id = Column(String, primary_key=True)
    order_products = Column(String)
    status = Column(String)
    payment = Column(String)
    table = Column(String)
    total = Column(Float)
    
Base.metadata.create_all(bind=engine)