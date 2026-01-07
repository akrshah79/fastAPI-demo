from fastapi import FastAPI
app3=FastAPI()
@app3.get("/")
async def measge():
    return {
        "message":"This is a query parameter example"
    }
@app3.get("/hello/{name}")
def hello(name:str,age:int):
    return {"name":name,"age":age}
#http://127.0.0.1:8000/hello/name?age=22