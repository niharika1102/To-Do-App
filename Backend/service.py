#has all the business logic for the todo app
from typing import List
from sqlalchemy.orm import sessionmaker

from models import Todo, Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)  # Create tables at module level

#database session generator
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoService:
    def __init__(self, db):
        """
        Constructor call
        """
        self.db = db
        
    def create_todo(self, todo_data):
        """Create a new todo item"""
        try:
            db_todo = Todo(
                title=todo_data.title,
                # description=todo_data.description,
                completed=todo_data.completed
            )
            self.db.add(db_todo)
            self.db.commit()
            self.db.refresh(db_todo)
            return db_todo
        except Exception as e:
            self.db.rollback()
            raise e
        
    def get_todos(self) -> List[Todo]:
        """Get all todos"""
        try:
            return self.db.query(Todo).all()
        except Exception as e:
            raise e
        
    def get_todo(self, todo_id: int) -> Todo: 
        """Get a specific todo by ID"""
        try:
            return self.db.query(Todo).filter(Todo.id == todo_id).first()
        except Exception as e:
            raise e
        
    def update_todo(self, todo_id: int, todo_data) -> Todo:
        """Update a todo item"""
        try:
            db_todo = self.get_todo(todo_id)
            if not db_todo:
                raise ValueError(f"Todo with id {todo_id} not found")
            
            if todo_data.title is not None:
                db_todo.title = todo_data.title
            # if todo_data.description is not None:
            #     db_todo.description = todo_data.description
            if todo_data.completed is not None:
                db_todo.completed = todo_data.completed

            self.db.commit()
            self.db.refresh(db_todo)
            return db_todo
        except Exception as e:
            self.db.rollback()
            raise e
                
    def delete_todo(self, todo_id: int) -> str:
        """Delete a todo item"""
        try:
            db_todo = self.get_todo(todo_id)
            if not db_todo:
                raise ValueError(f"Todo with id {todo_id} not found")
            
            self.db.delete(db_todo)
            self.db.commit()
            return f"Todo with id {todo_id} deleted successfully"
        except Exception as e:
            self.db.rollback()
            raise e
    
    def close(self):
        """Close the database session"""
        self.db.close()
