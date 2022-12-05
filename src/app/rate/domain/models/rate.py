from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey

Base = declarative_base()

class Rate(Base):
    __tablename__ = "rates"
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    parking_space_id = Column(Integer, ForeignKey("parking_space.id"))