from sqlalchemy import create_engine, Column, Integer, String, Float, DECIMAL, Text, TIMESTAMP, Enum, ForeignKey, Date
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Diamond(Base):
    __tablename__ = 'Diamonds'
    
    DiamondID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(255), nullable=False)
    Carat = Column(Float, nullable=False)
    Cut = Column(String(50), nullable=False)
    Color = Column(String(1), nullable=False)
    Clarity = Column(String(10), nullable=False)
    Price = Column(DECIMAL(15, 2), nullable=False)
    Stock = Column(Integer, nullable=False)
    Certificate = Column(String(255))
    Description = Column(Text)
    ImageURL = Column(String(500))
    CreatedAt = Column(TIMESTAMP, default=datetime.utcnow)
    UpdatedAt = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
