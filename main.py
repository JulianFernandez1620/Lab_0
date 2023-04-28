from fastapi import FastAPI
from model.user_connection import user_connection
from schema.user_schema import user_schema

app = FastAPI()
conn = user_connection()

@app.get("/")
def root():
    conn
    return "Welcome back Sir"

@app.post("/insert/usuario")
def insert(user_data: user_schema):
    print(user_data)