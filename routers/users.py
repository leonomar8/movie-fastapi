from fastapi import APIRouter
from pydantic import BaseModel
from user_jwt import createToken
from fastapi.responses import JSONResponse

login_user = APIRouter()

class User(BaseModel):
    email: str
    password: str


@login_user.post('/login', tags=['Authentication'])
def login(user: User):
    if user.email == 'omar@gmail.com' and user.password == '1234':
        token: str = createToken(user.dict())
        print (token)
        return JSONResponse(content=token)