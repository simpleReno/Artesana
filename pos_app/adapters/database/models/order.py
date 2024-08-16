import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine

class OrderEntity(Base):
    __tablename__ = 'Orders'

    id = Column(String, primary_key=True, unique=True)
    order_products = Column(String, ForeignKey('products.id'))
    product = relationship('Products', back_populates= 'orders')
    payment_id = Column(String, ForeignKey('payments.id'))
    payment = relationship('Payments', back_populates= 'orders')
    table_id = Column(String, ForeignKey('tables.id'))
    tables = relationship('Tables', back_populates= 'orders')
    status = Column(String)
    total = Column(Float)
    
Base.metadata.create_all(bind=engine)