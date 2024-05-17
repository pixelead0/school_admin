import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    amount = Column(Float)
    payment_id = Column(UUID(as_uuid=True), ForeignKey("payments.id"))
    date = Column(DateTime)

    student = relationship("Student", back_populates="invoices")
    payment = relationship("Payment")
    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
