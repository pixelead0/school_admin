# -*- coding: utf-8 -*-
import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Grade(Base):
    __tablename__ = "grades"
    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))

    school = relationship("School", back_populates="grades")
    students = relationship("Student", back_populates="grade")
    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
