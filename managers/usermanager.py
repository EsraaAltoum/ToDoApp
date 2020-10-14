import jwt
from fastapi import HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from jwt import ExpiredSignatureError, PyJWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database import get_db
from datamodel import USERDATUM
from model.models import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


def get(database, email):
    return database.query(USERDATUM).filter(USERDATUM.email == email).one_or_none()


def create(database, user: UserCreate):
    new_row = USERDATUM(
        email=user.email,
        password=pwd_context.hash(user.password),
        name=user.name
    )

    database.add(new_row)
    database.commit()


def confirmation(database, email, password):
    user= database.query(USERDATUM).filter(USERDATUM.email == email).one_or_none()

    if not user:
        raise HTTPException(status_code=401, detail= "Incorrect email")

    if not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail= "Incorrect password")

    return user

#decrypts token into user
def authenticate_user(token: str = Security(api_key_header)):
    try:
        payload = jwt.decode(token, 'fe8f2ba414d70f212356e6f2d82e1be0ae7d828c886672e8a117b1a4ccdbd02c', algorithms="HS256")
        value = payload.get("sub")
        if value is None:
            raise HTTPException(status_code=401, detail= "Invalid Credentials")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Your credentials have expired")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return value["user"]





