import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from pos_app.adapters.database.sqlite_adapter.connection import Base, engine

class EmployeeEntity(Base):
    __tablename__ = 'Employees'

    id = Column(Integer, primary_key=True, unique=True)
    turn_id = Column(Integer, ForeignKey('turn.id'))
    turn = relationship('Turns', back_populates= 'employees')
    start_date = Column(DateTime)
    Stop_date = Column(DateTime)
 
    
Base.metadata.create_all(bind=engine)