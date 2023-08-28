from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel, EmailStr, constr

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["classroom"]
collection = db["101"]

class Student(BaseModel):
    student_id: int
    name: str
    class_id: int
    classroom:int
    attendance: bool = False
    attendance_error: bool = False
    absent: bool = False

def create_student(student: Student):
    collection.insert_one(student.__dict__)

def get_students():
    return list(collection.find({}, {"_id": 0}))

def get_students_by_class(classroom: int):
    return list(collection.find({"classroom": classroom}, {"_id": 0}))

def get_students_by_name(name: str):
    return list(collection.find({"name": name}, {"_id": 0}))

def get_students_by_student_id(student_id: int):
    return list(collection.find({"student_id": student_id}, {"_id": 0}))

@app.post("/students/")
async def add_student(student: Student):
    create_student(student)
    return {"message": "Student added successfully"}

@app.get("/students/")
async def list_students():
    students = get_students()
    return {"students": students}

@app.get("/students/classroom/{classroom}")
async def list_students_by_class(classroom: int):
    students = get_students_by_class(classroom)
    if not students:
        raise HTTPException(status_code=404, detail="Class not found")
    return {"students": students}

@app.get("/students/name/{name}")
async def list_students_by_name(name: str):
    students = get_students_by_name(name)
    if not students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"students": students}

@app.get("/students/student_id/{student_id}")
async def list_students_by_student_id(student_id: int):
    students = get_students_by_student_id(student_id)
    if not students:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"students": students}

@app.get("/students/{classroom}")
async def list_students_by_class(classroom: int):
    students = get_students_by_class(classroom)
    if not students:
        raise HTTPException(status_code=404, detail="Class not found")
    return {"students": students}

@app.put("/students/attendance/{student_id}")
async def mark_attendance(student_id: int, attendance_data: dict):
    student = collection.find_one({"student_id": student_id})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    new_attendance = attendance_data.get("attendance", False)
    new_error = attendance_data.get("error", False)
    new_absent = attendance_data.get("absent", False) 
    
    collection.update_one(
        {"student_id": student_id},
        {"$set": {
            "attendance": new_attendance,
            "attendance_error": new_error,
            "absent": new_absent
        }}
    )
    return {"message": f"Attendance for student {student_id} updated"}