import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String, index=True)
    last_name_father = Column(String, index=True)
    last_name_mother = Column(String, index=True)
    enrollment = Column(String, unique=True)
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"))
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)

    school = relationship("School", back_populates="students")
    grade = relationship("Grade", back_populates="students")
    payments = relationship("Payment", back_populates="student")
    invoices = relationship("Invoice", back_populates="student")
