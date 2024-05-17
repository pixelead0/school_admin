# -*- coding: utf-8 -*-
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class InvoiceCreate(BaseModel):
    student_id: UUID = Field(...)
    amount: float = Field(...)
    payment_id: UUID = Field(...)
    date: datetime = Field(...)


class Invoice(BaseModel):
    id: UUID
    student_id: UUID
    amount: float
    payment_id: UUID
    date: datetime

    class Config:
        orm_mode = True
