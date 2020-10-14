from fastapi import APIRouter, Depends

from database import get_db
from managers.todomanager import create_task, query_tasks
from managers.usermanager import authenticate_user
from model.models import TaskCreate

router = APIRouter()


@router.post("/task")
def create_task_object(task: TaskCreate, database=Depends(get_db), user_id=Depends(authenticate_user)):
    create_task(database, task, user_id)

@router.get("/task")
def get_tasks(database=Depends(get_db), user_id=Depends(authenticate_user)):
    return query_tasks(database, user_id)
