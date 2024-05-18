import os
import uuid

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging_config import logger
from app.models.school import School
from app.schemas.school import SchoolCreate

PAGINATION_DEFAULT_LIMIT = settings.PAGINATION_DEFAULT_LIMIT


def get_school(db: Session, school_id: uuid.UUID):
    return db.query(School).filter(School.id == school_id).first()


def get_schools(db: Session, skip: int = 0, limit: int = PAGINATION_DEFAULT_LIMIT):
    return db.query(School).offset(skip).limit(limit).all()


def create_school(db: Session, school: SchoolCreate):
    db_school = School(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school


def update_school(db: Session, school_id: uuid.UUID, school_update: SchoolCreate):
    db_school = get_school(db, school_id)
    if db_school:
        for key, value in school_update.dict().items():
            setattr(db_school, key, value)
        db.commit()
        db.refresh(db_school)
    return db_school


def delete_school(db: Session, school_id: uuid.UUID):
    db_school = get_school(db, school_id)
    if db_school:
        db.delete(db_school)
        db.commit()
    return db_school
