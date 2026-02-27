import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from db.base import  Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    body = Column(String)
    is_published = Column(Boolean,default=False)
    is_deleted = Column(Boolean,default=False)
    created_at = Column(DateTime,default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    user = relationship("User", back_populates="posts")
    category = relationship("Category", back_populates =  "posts")
