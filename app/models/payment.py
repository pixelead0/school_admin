import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Payment(Base):
    __tablename__ = "payments"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))
    payment_type_id = Column(UUID(as_uuid=True), ForeignKey("payment_types.id"))

    student = relationship("Student", back_populates="payments")
    school = relationship("School", back_populates="payments")
    payment_type = relationship("PaymentType")
    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
