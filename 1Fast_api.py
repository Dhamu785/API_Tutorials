from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1:{"name":"kali","age":18,"class":"2nd year"},
    2:{"name":"John","age":17,"class":"1st year"},
    3:{"name":"Rock","age":19,"class":"3rd year"}
}

# Get data
@app.get("/")
def home():
    return{"Result": "Home Page"}

# Path parameter
@app.get("/get-student/{std_id}")
# def get_student(std_id:int = None):
def get_student(std_id:int = Path(description="Enter the student id",gt=0,lt=4)):
    return students[std_id]

# Query parameters
@app.get("/get-by-name")
# None is used to make the field is required to not required
# Here Optional is used to make code readable
def get_by_name(*, name: Optional[str]=None, test: int): 
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return{f"{name}": "Not found"}