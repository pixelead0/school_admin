from uuid import UUID

from pydantic import BaseModel, Field, constr


class GradeCreate(BaseModel):
    name: constr(min_length=1) = Field(...)
    school_id: UUID = Field(...)


class Grade(BaseModel):
    id: UUID
    name: str
    school_id: UUID

    class Config:
        orm_mode = True
