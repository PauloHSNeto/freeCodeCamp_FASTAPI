import fastapi
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

api = FastAPI()

students={
    1:{
        "name":"Paulo",
        "age": 32,
        "isActive" :True,
    },
    2:{
        "name":"Aleister",
        "age":36,
        "isActive":True,
    },
    3:{
        "name":"Tim",
        "age": 37,
        "isActive":False,
    },
    4:{
        "name":"Felix",
        "age": 34,
        "isActive":True,
    }
}

class StudentModel(BaseModel):
    name:str
    age:int
    isActive:bool

@api.get("/")
def index():
    return{"name":"FirstData"}

@api.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=5)):
    return students[student_id]


@api.get("/get-by-name/{student_id}")
def get_student(*,student_id: int,name:Optional[str]=None,test:int):
    for id in students:
        if students[id]["name"]==name:
            return students[id]
    return {"Data":"Not found"}


@api.post("/create-student/{student_id}")
def create_student(id:int, newStudent: StudentModel):
    if id in students:
        return {"Wrong ID"}
    students[id]= newStudent
    return students[id]