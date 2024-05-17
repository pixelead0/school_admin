import uuid
from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class SchoolPeriodType(enum.Enum):
    bimestral = "bimestral"
    trimestral = "trimestral"
    cuatrimestral = "cuatrimestral"
    semestral = "semestral"

class School(Base):
    __tablename__ = "schools"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    country = Column(String)
    state = Column(String)
    description = Column(String)
    period_type = Column(Enum(SchoolPeriodType))

    students = relationship("Student", back_populates="school")
    payments = relationship("Payment", back_populates="school")
    grades = relationship("Grade", back_populates="school")
    user = relationship("User", back_populates="school", uselist=False)
