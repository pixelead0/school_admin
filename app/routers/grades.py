# -*- coding: utf-8 -*-
import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.grade import (create_grade, delete_grade, get_grade, get_grades,
                            update_grade)
from app.db.session import get_db
from app.schemas.grade import Grade, GradeCreate

router = APIRouter()


@router.get("/grades/{school_id}", response_model=List[Grade])
def read_grades(school_id: uuid.UUID, skip: int = 0, limit: int = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10)), db: Session = Depends(get_db)):
    grades = get_grades(db, school_id=school_id, skip=skip, limit=limit)
    return grades


@router.post("/grades/", response_model=Grade)
def create_grade_endpoint(grade: GradeCreate, db: Session = Depends(get_db)):
    return create_grade(db=db, grade=grade)


@router.get("/grades/detail/{grade_id}", response_model=Grade)
def read_grade(grade_id: uuid.UUID, db: Session = Depends(get_db)):
    db_grade = get_grade(db, grade_id=grade_id)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade


@router.delete("/grades/{grade_id}", response_model=Grade)
def delete_grade_endpoint(grade_id: uuid.UUID, db: Session = Depends(get_db)):
    db_grade = delete_grade(db=db, grade_id=grade_id)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade


@router.put("/grades/{grade_id}", response_model=Grade)
def update_grade_endpoint(grade_id: uuid.UUID, grade: GradeCreate, db: Session = Depends(get_db)):
    db_grade = update_grade(db=db, grade_id=grade_id, grade_update=grade)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade
