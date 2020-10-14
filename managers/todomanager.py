from datamodel import TODO
from model.models import TaskCreate


def create_task(database, task: TaskCreate, user_id):
    new_row = TODO(
        task=task.task,
        priority=task.priority,
        due_date=task.due_date,
        note=task.note,
        status_id=1,
        user_data_id=user_id,
    )
    database.add(new_row)
    database.commit()


def query_tasks(database, user_data_id):
    return database.query(TODO).filter(TODO.user_data_id == user_data_id).all()
