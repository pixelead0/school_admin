import uuid
from sqlalchemy import Column, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    amount = Column(Float)
    payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.id"))
    date = Column(DateTime)

    student = relationship("Student", back_populates="invoices")
    payment = relationship("Payment")
