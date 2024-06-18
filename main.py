from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from user_jwt import createToken
from bd.database import engine, Base
from routers.movie import routerMovie
from routers.users import login_user
import uvicorn
import os


app = FastAPI(
    title='Aprendizaje FastAPI',
    description='Proyecto de Aprendizaje FastAPI',
    version='0.0.1'
)

app.include_router(routerMovie)
app.include_router(login_user)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Inicio'])
def read_root():
    return {'Hello': 'World'}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
