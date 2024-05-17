# -*- coding: utf-8 -*-
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
    period_type: SchoolPeriodType = Field(...)


class School(BaseModel):
    id: UUID
    name: str
    country: str
    state: str
    description: str
    period_type: SchoolPeriodType

    class Config:
        orm_mode = True
