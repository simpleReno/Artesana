import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine

class PaymentEntity(Base):
    __tablename__ = 'Payments'

    id = Column(String, primary_key=True, unique=True)
    payment_type = Column(String)
    order_id = Column(String, ForeignKey('orders.id'))
    order = relationship('Orders', back_populates= 'payments')
    payment_amount = Column(Float, ForeignKey('Orders.total'))
    amount = relationship('Orders', back_populates= 'payments')
    description = Column(String)
 
    
Base.metadata.create_all(bind=engine)