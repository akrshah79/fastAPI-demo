from fastapi import FastAPI,Path
app4=FastAPI()
@app4.get("/")
async def measge():
    return {
        "message":"This is a query parameter example"
    }
@app4.get("/hello/{name}")
def hello(name:str=Path(...,min_length=2,max_length=10),age:int=0):
    return {"name":name,"age":age}
#http://127.0.0.1:8000/hello/name?age=22