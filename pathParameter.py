from fastapi import FastAPI
app2=FastAPI()
@app2.get("/")
async def message():
    return {
        "message":"This is a path parameter example"
    }


@app2.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
    return {"name":name,"age":age}