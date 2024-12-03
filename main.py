from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI()

# In-memory store for tasks
tasks = []

# Define the Task model
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    created_at: datetime
    due_date: Optional[datetime] = None
    is_completed: bool = False

    @property
    def remaining_days(self):
        if self.due_date:
            delta = self.due_date - datetime.now()
            return delta.days
        return None


    

# Create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Read all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

# Read a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# Update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    return task

# Delete a task by ID
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks.pop(task_id)
    return deleted_task
