# app/main.py

from fastapi import FastAPI
from routes import auth_route, plats_route

app = FastAPI()

app.include_router(auth_route.router, prefix="/auth")
app.include_router(plats_route.router, prefix="/api")
