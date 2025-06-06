from fastapi import FastAPI
from project.task import api

app = FastAPI()

app.include_router(api.router)
