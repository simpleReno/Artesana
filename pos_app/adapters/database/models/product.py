import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine




class ProductEntity(Base):
    __tablename__ = 'Products'

    id = Column(String, primary_key=True, unique= True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    category_id = Column(String, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
    
Base.metadata.create_all(bind=engine)
    