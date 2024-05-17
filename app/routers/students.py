from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.student import Student, StudentCreate
from app.crud.student import get_student, get_students, create_student, delete_student, update_student
from app.db.session import get_db
from typing import List
import uuid
import os

router = APIRouter()

@router.get("/students/", response_model=List[Student])
def read_students(skip: int = 0, limit: int = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10)), db: Session = Depends(get_db)):
    students = get_students(db, skip=skip, limit=limit)
    return students

@router.post("/students/", response_model=Student)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db=db, student=student)

@router.get("/students/{student_id}", response_model=Student)
def read_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    db_student = get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/students/{student_id}", response_model=Student)
def delete_student_endpoint(student_id: uuid.UUID, db: Session = Depends(get_db)):
    db_student = delete_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.put("/students/{student_id}", response_model=Student)
def update_student_endpoint(student_id: uuid.UUID, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = update_student(db=db, student_id=student_id, student_update=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student
