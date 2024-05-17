from uuid import UUID

from pydantic import BaseModel, Field


class PaymentCreate(BaseModel):
    student_id: UUID = Field(...)
    school_id: UUID = Field(...)
    payment_type_id: UUID = Field(...)


class Payment(BaseModel):
    id: UUID
    student_id: UUID
    school_id: UUID
    payment_type_id: UUID

    class Config:
        orm_mode = True
