from sqlalchemy import Column,Integer,String

from config import Base
class Book(Base):
    __tablename = "book"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    dis = Column(String)
    