# -*- coding: utf-8 -*-
import os
import uuid

from sqlalchemy.orm import Session

from app.models.grade import Grade
from app.schemas.grade import GradeCreate

PAGINATION_DEFAULT_LIMIT = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10))


def get_grade(db: Session, grade_id: uuid.UUID):
    return db.query(Grade).filter(Grade.id == grade_id).first()


def get_grades(db: Session, school_id: uuid.UUID, skip: int = 0, limit: int = PAGINATION_DEFAULT_LIMIT):
    return db.query(Grade).filter(Grade.school_id == school_id).offset(skip).limit(limit).all()


def create_grade(db: Session, grade: GradeCreate):
    db_grade = Grade(
        id=uuid.uuid4(),
        name=grade.name,
        school_id=grade.school_id
    )
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade


def delete_grade(db: Session, grade_id: uuid.UUID):
    db_grade = get_grade(db, grade_id)
    if db_grade:
        db.delete(db_grade)
        db.commit()
    return db_grade


def update_grade(db: Session, grade_id: uuid.UUID, grade_update: GradeCreate):
    db_grade = get_grade(db, grade_id)
    if db_grade:
        db_grade.name = grade_update.name
        db_grade.school_id = grade_update.school_id
        db.commit()
        db.refresh(db_grade)
    return db_grade
