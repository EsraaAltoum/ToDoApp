import datetime
import json

import jwt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from database import get_db
from managers.usermanager import get, create, confirmation
from model.models import UserCreate

router = APIRouter()

#query parameter
@router.get("/user")
def get_user(email: str, database = Depends(get_db)):
    user = get(database, email)
    return user


@router.post("/user")
def create_user(user: UserCreate, database = Depends(get_db)):
    create(database, user)

# omar was here

@router.post("/signin")
def confirm_user(form_data: OAuth2PasswordRequestForm = Depends(), database = Depends(get_db)):
    user = confirmation(database,form_data.username, form_data.password )

#creation of JSON object and encoding it into JWT token
    to_encode = {"sub": {"user": user.user_data_id}}
    expiry_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
    to_encode.update({"exp": expiry_time})
    encoded_jwt = jwt.encode(to_encode, "fe8f2ba414d70f212356e6f2d82e1be0ae7d828c886672e8a117b1a4ccdbd02c", algorithm="HS256", json_encoder=JSONEncoder)
    return {"access_token": encoded_jwt, "user": user}

#JSON encoder class for datetime
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

