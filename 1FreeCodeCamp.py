from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import uvicorn

# uvicorn documentation https://www.uvicorn.org/
# YouTube https://youtu.be/tLKKmouUams
# Postman(YT) https://youtu.be/VywxIQ2ZXw4
app = FastAPI()

class Student(BaseModel):
    name : str
    age : int
    year : str
    
class UpdateStudents(BaseModel):
    name : Optional[str]=None
    age : Optional[int]=None
    year : Optional[str]=None
    
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
    
# Put method used to update already existing data
@app.put("/update-student/{student_id}")
def update_student(student_id: int, update_details: UpdateStudents):
    if student_id not in students:
        return{"Error":"Student not exists"}
    else:
        if update_details.name != None:
            students[student_id]['name']= update_details.name
        if update_details.age != None:
            students[student_id]['age']= update_details.age
        if update_details.year != None:
            students[student_id]['year']= update_details.year
        return{"Succes":"Updated successfully"}
    
# Delete the student details
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return{"Error":"Student id does not exists"}
    else:
        del students[student_id]
        return{"Message":"Student data deleted successfully"}

# If the below codes does not exists you can use "uvicorn file_name:app --reload" in the command prompt
if __name__ == "__main__":
    uvicorn.run("1FreeCodeCamp:app", port=5000, log_level="info",reload=True)
