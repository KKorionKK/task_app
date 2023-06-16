from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, Mapped
from typing import List
from .item_model import Item

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    surname = Column(String(64))
    email = Column(String(128))
    password = Column(String(256))
    active = Column(Boolean)
    created = Column(DateTime(timezone=False))
    
