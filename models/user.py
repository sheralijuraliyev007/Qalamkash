from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    bio = Column(String, nullable=True)
    img_url = Column(String, nullable=True)
    is_creator = Column(Boolean,default=False)
    hashed_password = Column(String,nullable=False)

