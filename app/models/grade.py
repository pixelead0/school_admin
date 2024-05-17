import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class Grade(Base):
    __tablename__ = "grades"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))

    school = relationship("School", back_populates="grades")
    students = relationship("Student", back_populates="grade")
