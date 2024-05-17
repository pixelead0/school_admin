from pydantic import BaseModel, Field, constr
from uuid import UUID

class PaymentTypeCreate(BaseModel):
    name: constr(min_length=2) = Field(...)
    price: float = Field(...)

class PaymentType(BaseModel):
    id: UUID
    name: str
    price: float

    class Config:
        orm_mode = True
