import uuid
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    payment_type_id = Column(UUID(as_uuid=True), ForeignKey("payment_types.id"))

    student = relationship("Student", back_populates="payments")
    school = relationship("School", back_populates="payments")
    payment_type = relationship("PaymentType")
