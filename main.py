from fastapi import FastAPI
from model.user_connection import user_connection
from schema.user_schema import user_schema

app = FastAPI()
conn = user_connection()

@app.get("/")
def root():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items

@app.get("/api/user/{id}")
def read_one(id:str):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return dictionary

@app.post("/insert/usuario")
def insert(user_data: user_schema):
    data = user_data.dict()
    data.pop("id")
    conn.write(data)

@app.delete("/api/delete/{id}")
def delete(id:str):
    conn.delete(id)

@app.put("/api/update/{id}")
def update(user_data:user_schema , id:str):
    data = user_data.dict()
    data["id"] = id
    conn.update(data)