from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    header = Column(String(64))
    description = Column(String(512))
    status = Column(Boolean)
    created = Column(DateTime(timezone=False))
    deadline = Column(DateTime(timezone=False))

    user_id = Column(Integer, ForeignKey('users.id'))
