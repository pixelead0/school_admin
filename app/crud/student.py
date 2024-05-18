import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.student import Student
from app.schemas.student import StudentCreate


def get_student(db: Session, student_id: uuid.UUID):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


def get_students(
    db: Session,
    skip: int = 0,
    limit: int = settings.PAGINATION_DEFAULT_LIMIT,
):
    return db.query(Student).offset(skip).limit(limit).all()


def create_student(db: Session, student: StudentCreate):
    try:
        db_student = Student(
            id=uuid.uuid4(),
            first_name=student.first_name,
            last_name_father=student.last_name_father,
            last_name_mother=student.last_name_mother,
            enrollment=student.enrollment,
            grade_id=student.grade_id,
            school_id=student.school_id,
            user_id=student.user_id,
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating student: {str(e)}",
        )


def delete_student(db: Session, student_id: uuid.UUID):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student


def update_student(db: Session, student_id: uuid.UUID, student_update: StudentCreate):
    db_student = get_student(db, student_id)
    if db_student:
        db_student.first_name = student_update.first_name
        db_student.last_name_father = student_update.last_name_father
        db_student.last_name_mother = student_update.last_name_mother
        db_student.enrollment = student_update.enrollment
        db_student.grade_id = student_update.grade_id
        db_student.school_id = student_update.school_id
        db_student.user_id = student_update.user_id
        db.commit()
        db.refresh(db_student)
    return db_student
