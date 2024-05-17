import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.school import (
    create_school,
    delete_school,
    get_school,
    get_schools,
    update_school,
)
from app.db.session import get_db
from app.schemas.school import School, SchoolCreate

router = APIRouter()


@router.get("/schools/", response_model=List[School])
def read_schools(
    skip: int = 0,
    limit: int = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10)),
    db: Session = Depends(get_db),
):
    schools = get_schools(db, skip=skip, limit=limit)
    return schools


@router.post("/schools/", response_model=School)
def create_school_endpoint(school: SchoolCreate, db: Session = Depends(get_db)):
    return create_school(db=db, school=school)


@router.get("/schools/{school_id}", response_model=School)
def read_school(school_id: uuid.UUID, db: Session = Depends(get_db)):
    db_school = get_school(db, school_id=school_id)
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school


@router.delete("/schools/{school_id}", response_model=School)
def delete_school_endpoint(school_id: uuid.UUID, db: Session = Depends(get_db)):
    db_school = delete_school(db=db, school_id=school_id)
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school


@router.put("/schools/{school_id}", response_model=School)
def update_school_endpoint(
    school_id: uuid.UUID,
    school: SchoolCreate,
    db: Session = Depends(get_db),
):
    db_school = update_school(db=db, school_id=school_id, school_update=school)
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school
