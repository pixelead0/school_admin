import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Student(Base):
    __tablename__ = "student"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    first_name = Column(String(100), index=True)
    last_name_father = Column(String(100), index=True)
    last_name_mother = Column(String(100), index=True)
    enrollment = Column(String, unique=True)
    # grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"))
    # school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    # user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)

    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
