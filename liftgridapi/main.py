from fastapi import FastAPI
from fastapi_pagination import add_pagination
from liftgridapi.routers import api_router

app = FastAPI(title = 'liftGridApi')
app.include_router(api_router)


add_pagination(app)