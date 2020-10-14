from fastapi import HTTPException
from passlib.context import CryptContext

from datamodel import STATUS

#queries database and returns all "status" options
def query_status(database):
    return database.query(STATUS).all()

def query_single_status(database, id):
    return database.query(STATUS).filter(STATUS.status_id == id).one_or_none()