import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
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
    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
