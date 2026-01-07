from fastapi import FastAPI, Path
from typing import Optional
app=FastAPI()
@app.get("/hello")
async def hello():
    return {"message":"Hello"}
#Path Parameter
@app.get("/hello/{name}")
async def world(name:str):
    return {"message":"Hello "+name}
#Query Parameter
@app.get("/geet")
async def greet(name:str,age:int):
    return {"name":name,
            "age":age}
#Optional Query Parameter
@app.get("/greet")
async def greet(name:str=Path(...,min_length=2,max_length=10), age: Optional[int] = None):
    return {"name": name, "age": age}
#Parameter Validation
@app.get("/items/{item_id}")
async def read_items(item_id:int=Path(...,title="The ID of the item to get",ge=1,le=1000)):
    return {"item_id":item_id}
#Query Parameter
