# -*- coding: utf-8 -*-
import os
import uuid

from sqlalchemy.orm import Session

from app.models.school import School
from app.schemas.school import SchoolCreate

PAGINATION_DEFAULT_LIMIT = int(os.getenv("PAGINATION_DEFAULT_LIMIT", 10))


def get_school(db: Session, school_id: uuid.UUID):
    return db.query(School).filter(School.id == school_id).first()


def get_schools(db: Session, skip: int = 0, limit: int = PAGINATION_DEFAULT_LIMIT):
    return db.query(School).offset(skip).limit(limit).all()


def create_school(db: Session, school: SchoolCreate):
    db_school = School(
        id=uuid.uuid4(),
        name=school.name,
        country=school.country,
        state=school.state,
        description=school.description,
        period_type=school.period_type
    )
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school


def delete_school(db: Session, school_id: uuid.UUID):
    db_school = get_school(db, school_id)
    if db_school:
        db.delete(db_school)
        db.commit()
    return db_school


def update_school(db: Session, school_id: uuid.UUID, school_update: SchoolCreate):
    db_school = get_school(db, school_id)
    if db_school:
        db_school.name = school_update.name
        db_school.country = school_update.country
        db_school.state = school_update.state
        db_school.description = school_update.description
        db_school.period_type = school_update.period_type
        db.commit()
        db.refresh(db_school)
    return db_school
