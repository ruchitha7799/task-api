from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="Simple CRUD API using FastAPI",
    version="1.0"
)

# ======================================================
# Response Models
# ======================================================

class Task(BaseModel):
    id: int
    title: str
    done: bool


class APIInfo(BaseModel):
    name: str
    version: str
    endpoints: List[str]


class HealthResponse(BaseModel):
    status: str


# ======================================================
# Request Models
# ======================================================

class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


# ======================================================
# In-Memory Database
# ======================================================

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete Assignment",
        "done": False
    },
    {
        "id": 3,
        "title": "Practice Python",
        "done": True
    }
]


# ======================================================
# Root Endpoint
# ======================================================

@app.get(
    "/",
    response_model=APIInfo,
    summary="API Information",
    description="Returns the API name, version and available endpoints."
)
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


# ======================================================
# Health Check
# ======================================================

@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Checks whether the API server is running."
)
def health():
    return {
        "status": "ok"
    }


# ======================================================
# Get All Tasks
# ======================================================

@app.get(
    "/tasks",
    response_model=List[Task],
    summary="Get All Tasks",
    description="Returns all tasks from the in-memory database."
)
def get_tasks():
    return tasks


# ======================================================
# Get Task By ID
# ======================================================

@app.get(
    "/tasks/{id}",
    response_model=Task,
    summary="Get Task By ID",
    description="Returns a single task using its ID."
)
def get_task(id: int):

    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )


# ======================================================
# Create Task
# ======================================================

@app.post(
    "/tasks",
    response_model=Task,
    status_code=201,
    summary="Create Task",
    description="Creates a new task."
)
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_id = tasks[-1]["id"] + 1 if tasks else 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# ======================================================
# Update Task
# ======================================================

@app.put(
    "/tasks/{id}",
    response_model=Task,
    summary="Update Task",
    description="Updates an existing task."
)
def update_task(id: int, updated_task: TaskUpdate):

    if updated_task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    for task in tasks:

        if task["id"] == id:
            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )


# ======================================================
# Delete Task
# ======================================================

@app.delete(
    "/tasks/{id}",
    status_code=204,
    summary="Delete Task",
    description="Deletes a task using its ID."
)
def delete_task(id: int):

    for task in tasks:

        if task["id"] == id:
            tasks.remove(task)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )