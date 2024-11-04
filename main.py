from fastapi import FastAPI, HTTPException
from models import TodoItem
from typing import List

app = FastAPI()

todo_db = []

@app.get("/")
def home():
    return {"message": "Hello, World!"}

# Create a ToDo item
@app.post("/todos/", response_model=TodoItem)
async def create_todo(item: TodoItem):
    todo_db.append(item)
    return item

# Get all ToDo items
@app.get("/todos/", response_model=List[TodoItem])
async def read_todos():
    return todo_db

# Get a single ToDo item by ID
@app.get("/todos/{item_id}", response_model=TodoItem)
async def read_todo(item_id: int):
    for item in todo_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="ToDo item not found")

# Update a ToDo item by ID
@app.put("/todos/{item_id}", response_model=TodoItem)
async def update_todo(item_id: int, updated_item: TodoItem):
    for index, item in enumerate(todo_db):
        if item.id == item_id:
            todo_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="ToDo item not found")

# Delete a ToDo item by ID
@app.delete("/todos/{item_id}")
async def delete_todo(item_id: int):
    for index, item in enumerate(todo_db):
        if item.id == item_id:
            del todo_db[index]
            return {"message": "ToDo item deleted"}
    raise HTTPException(status_code=404, detail="ToDo item not found")
