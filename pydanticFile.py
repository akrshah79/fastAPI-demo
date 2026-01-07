from pydantic import BaseModel,Field
from typing import Annotated
class Student(BaseModel):
    name:str=Field(...,min_length=2,max_length=10)
    #age:int=Field(...,gt=0, le=100)
    age:Annotated[int,Field(...,gt=0,le=100)]
    subjects:list[str]=Field(...,min_items=1,max_items=5)       