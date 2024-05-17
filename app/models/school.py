import enum
import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class SchoolPeriodType(enum.Enum):
    bimestral = "bimestral"
    trimestral = "trimestral"
    cuatrimestral = "cuatrimestral"
    semestral = "semestral"


class School(Base):
    __tablename__ = "schools"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = Column(String, index=True)
    country = Column(String)
    state = Column(String)
    description = Column(String)
    period_type = Column(Enum(SchoolPeriodType))

    students = relationship("Student", back_populates="school")
    payments = relationship("Payment", back_populates="school")
    grades = relationship("Grade", back_populates="school")
    user = relationship("User", back_populates="school", uselist=False)
    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
