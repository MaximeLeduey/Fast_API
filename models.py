from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    publication_date = Column(Date)

    items = relationship("Item", back_populates="owner")