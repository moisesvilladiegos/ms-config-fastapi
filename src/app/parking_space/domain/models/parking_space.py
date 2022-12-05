from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class ParkingSpace(Base):
    __tablename__ = "parking_space"
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    count = Column(Integer)