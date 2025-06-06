from .crud import get_task_by_id

def mark_task_as_completed(task_id: int, db):
    task = get_task_by_id(db, task_id)
    if not task:
        raise ValueError("Tarea no encontrada")
    task.completed = True
    db.commit()
