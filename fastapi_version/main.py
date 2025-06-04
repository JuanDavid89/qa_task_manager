from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from collections import OrderedDict

app = FastAPI()

# Modelo Pydantic para las tareas (sin id, que se autogenera)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""

# Modelo Pydantic para las tareas con id
class Task(TaskCreate):
    id: int

tasks: List[Task] = []

@app.get("/tasks")
def get_tasks():
    return [
        OrderedDict([
            ('id', task.id),
            ('title', task.title),
            ('description', task.description),
        ]) for task in tasks
    ]


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_id = len(tasks) + 1
    new_task = Task(id=new_id, **task.model_dump())
    tasks.append(new_task)

    # Devolver OrderedDict para mantener orden
    ordered_response = OrderedDict([
        ('id', new_task.id),
        ('title', new_task.title),
        ('description', new_task.description),
    ])

    return ordered_response
