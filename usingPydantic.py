from fastapi import FastAPI
from typing import List
from pydanticFile import Student
a:list[Student]=[]
app5=FastAPI()
@app5.get("/")
async def message():
    return{
        "message":"This is a pydantic model example"
    }
@app5.post("/student")
async def create_student(student:Student):
    a.append(student)
    return a
@app5.get("/students")
async def get_students():
    return a