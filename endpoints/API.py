from fastapi import APIRouter

from endpoints.userdata import router as user_router
from endpoints.status import router as status_router
from endpoints.todolist import router as todo_router

router = APIRouter()
router.include_router(user_router)
router.include_router(status_router)
router.include_router(todo_router)