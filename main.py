from fastapi import FastAPI
app1=FastAPI()
@app1.get("/")
async def index():
    return {"message":"Hello World"}
