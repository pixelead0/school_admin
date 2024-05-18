import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Payment(Base):
    __tablename__ = "payment"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    student_id = Column(UUID(as_uuid=True), ForeignKey("student.id"))
    school_id = Column(UUID(as_uuid=True), ForeignKey("school.id"))
    payment_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("payment_type.id"),
    )

    # Audit Fields
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
