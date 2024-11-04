from sqlalchemy import Column, Integer, String
from database import Base

# Define the Todo model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(255))
