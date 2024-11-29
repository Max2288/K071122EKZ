from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from crud import (
    get_student_hobbies,
    delete_student,
    add_student,
    add_hobby,
    assign_hobby_to_student,
)

app = FastAPI()

router = APIRouter(prefix='/api/v1')


class StudentCreate(BaseModel):
    name: str

class HobbyCreate(BaseModel):
    name: str

class AssignHobby(BaseModel):
    student_id: int
    hobby_id: int

@router.get("/students/{student_id}/hobbies")
def read_student_hobbies(student_id: int):
    hobbies = get_student_hobbies(student_id)
    if not hobbies:
        raise HTTPException(status_code=404, detail="Student not found or no hobbies")
    return hobbies

@router.delete("/students/{student_id}")
def remove_student(student_id: int):
    try:
        delete_student(student_id)
        return {"message": f"Student {student_id} deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/students")
def create_student(student: StudentCreate):
    try:
        student_id = add_student(student.name)
        return {"id": student_id, "name": student.name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/hobbies")
def create_hobby(hobby: HobbyCreate):
    try:
        hobby_id = add_hobby(hobby.name)
        return {"id": hobby_id, "name": hobby.name}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/students/{student_id}/hobbies/{hobby_id}")
def assign_hobby(student_id: int, hobby_id: int):
    try:
        assign_hobby_to_student(student_id, hobby_id)
        return {"message": f"Hobby {hobby_id} assigned to student {student_id}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)