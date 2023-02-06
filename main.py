from typing import Union
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient


config= dotenv_values(".env")

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Welcome  manage package !"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database !")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(book_router, tags=["encomenda"], prefix="/encomendas")