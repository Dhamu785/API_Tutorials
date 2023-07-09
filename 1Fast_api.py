from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1:{"name":"kali","age":18,"class":"2nd year"},
    2:{"name":"John","age":17,"class":"1st year"},
    3:{"name":"Rock","age":19,"class":"3rd year"}
}

@app.get("/")
def home():
    return{"Result": "Home Page"}

@app.get("/get-student/{std_id}")
def get_student(std_id:int = Path(description="Enter the student id",gt=0,lt=4)):
    return students[std_id]