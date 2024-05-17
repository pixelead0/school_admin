import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    school_id = Column(UUID(as_uuid=True), ForeignKey("schools.id"))

    school = relationship("School", back_populates="user")
