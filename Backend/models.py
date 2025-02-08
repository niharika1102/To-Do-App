#has all the models for the todo app(pydantic models and sqlalchemy models)
from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
CONNECTION_STRING = "postgresql://temporal:temporal@localhost:5432/postgres"
engine = create_engine(CONNECTION_STRING)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# get_db should be added here

# SQLAlchemy model

class Todo(Base):
    """
    Todo table generated for the database
    """
    __tablename__="task"
    id=Column(Integer, primary_key=True)
    title=Column(String)
    # description=Column(String)
    completed=Column(Boolean, default=False)

#defining pydantic models
# tells that the class is a schema
class TodoBase(BaseModel):
    """
    Todo base model for validation of request
    """
    id: Optional[int] = None
    title: str
    # description: Optional[str] = Field(None, max_length=100)
    completed: bool
    
class TodoCreate(TodoBase):
    """
    Todo create model for validation of request
    """
    pass  #passing all data from the base model as it is

class TodoUpdate(TodoBase):
    """
    Todo update model for validation of request
    """
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    # description: Optional[str] = Field(None, max_length=100)
    completed: Optional[bool] = None
    
#pydantic model for how the reponse of any request giving back the task will look like
class TodoResponse(TodoBase):
    """
    Todo response model for validation of response
    """
    id: int
    title: str
    # description: Optional[str] = None
    completed: bool

    class Config:
        from_attributes = True
