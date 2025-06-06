from typing import List
from .schemas import Task, TaskCreate

tasks_db: List[Task] = []

def get_tasks() -> List[Task]:
    return tasks_db

def create_task(task: TaskCreate) -> Task:
    new_task = Task(id=len(tasks_db) + 1, **task.model_dump())
    tasks_db.append(new_task)
    return new_task
