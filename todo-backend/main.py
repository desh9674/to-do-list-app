from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from db_connection import db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

class Task(BaseModel):
    id: Optional[str] = None  # Add the id field here
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

def task_serializer(task) -> dict:
    return {
        "id": str(task["_id"]),  # Converts _id to id
        "title": task["title"],
        "description": task.get("description"),
        "created_at": task["created_at"],
        "due_date": task.get("due_date"),
        "is_completed": task["is_completed"]
    }

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task_dict = task.model_dump(exclude_unset=True)
    task_dict['created_at'] = datetime.now()
    result = db.tasks.insert_one(task_dict)
    task_dict["_id"] = result.inserted_id
    return task_serializer(task_dict)

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    tasks = db.tasks.find()
    return [task_serializer(task) for task in tasks]

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    task = db.tasks.find_one({"_id": ObjectId(task_id)})
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_serializer(task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task: Task):
    task_dict = task.model_dump(exclude_unset=True)
    result = db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": task_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    task_dict["_id"] = ObjectId(task_id)
    return task_serializer(task_dict)

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: str):
    task = db.tasks.find_one_and_delete({"_id": ObjectId(task_id)})
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_serializer(task)







 