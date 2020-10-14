from fastapi import APIRouter, Depends

from database import get_db
from managers.statusmanager import query_status, query_single_status

router = APIRouter()

@router.get("/status")
def get_status(database= Depends(get_db)):
    status = query_status(database)
    return status

#path parameter
@router.get("/status/{id}")
def get_single_status(id: int, database= Depends(get_db)):
    return query_single_status(database, id)


