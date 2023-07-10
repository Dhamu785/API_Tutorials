from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name : str
    age : int
    year : str
    
students = {
    1:{"name":"kali","age":18,"year":"2nd year"},
    2:{"name":"John","age":17,"year":"1st year"},
    3:{"name":"Rock","age":19,"year":"3rd year"}
}

# Get data
@app.get("/")
def home():
    return{"Result": "Home Page"}

# Path parameter
@app.get("/get-student/{std_id}")
# def get_student(std_id:int = None):
def get_student(std_id:int = Path(description="Enter the student id",gt=0,lt=24)):
    return students[std_id]

# Query parameters
@app.get("/get-by-name")
# None is used to make the field is required to not required
# Here Optional is used to make code readable
# def get_by_name(*, name: Optional[str]=None, test: int): I deleted "test" to run properly
def get_by_name(*, name: Optional[str]=None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return{f"{name}": "Not found"}

# Get by both path parm(pp) and query parm(qp)
@app.get("/get-by-pp-qp/{std_id}")
def get_by_name(*, std_id:int , name: Optional[str]=None):
    for student_id in students:
        if students[student_id]['name'] == name and student_id==std_id:
            return students[student_id]
    return{f"{name}": "Not found"}

# Post method used to upload data to the database through API
@app.post("/add-student/{student_id}")
def add_student(student_id : int, student_details : Student):
    if student_id in students:
        return {"Error":"Id already exists"}
    else:
        students[student_id] = student_details
        return{"Sucess":f"Student {student_details.name} added"}