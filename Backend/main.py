from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from models import TodoResponse, TodoCreate, TodoUpdate
from service import TodoService, get_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the router
@app.get("/")
def home():
    return "Welcome to the Todo API"

@app.get("/todos", response_model=List[TodoResponse])  #response model is the pydantic model for the response
def get_all_todos(db: Session = Depends(get_db)):
    # Create an object of TodoService class
    service = TodoService(db)
    try:
        todos = service.get_todos()  #calls the get_todos method from the service.py to get all the todos
        return todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/todos/{id}", response_model=TodoResponse)
def get_todo(id: int, db: Session = Depends(get_db)):
    service = TodoService(db)
    try:
        todo = service.get_todo(id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/todos/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    service = TodoService(db)
    try:
        return service.create_todo(todo)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/todos/{id}", response_model=TodoResponse)
def update_todo(id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    service = TodoService(db)
    try:
        updated_todo = service.update_todo(id, todo_update)
        if not updated_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return updated_todo
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/todos/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    service = TodoService(db)
    try:
        result = service.delete_todo(id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # to run the server
