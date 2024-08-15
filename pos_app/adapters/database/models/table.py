import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine

class TableEntity(Base):
    __tablename__ = 'Tables'
    
    id = Column(String, primary_key= True, unique= True)
    orders_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Orders', back_populates='tables')
    
Base.metadata.create_all(bind=engine)