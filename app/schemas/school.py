from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field, constr


class SchoolPeriodType(str, Enum):
    bimestral = "bimestral"
    trimestral = "trimestral"
    cuatrimestral = "cuatrimestral"
    semestral = "semestral"


class SchoolCreate(BaseModel):
    name: constr(min_length=2) = Field(...)
    country: constr(min_length=2) = Field(...)
    state: constr(min_length=2) = Field(...)
    description: str = Field(...)


class School(BaseModel):
    id: UUID
    name: str
    country: str
    state: str
    description: str

    class Config:
        orm_mode = True
