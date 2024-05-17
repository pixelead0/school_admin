from pydantic import BaseModel, Field, constr
from uuid import UUID

class StudentCreate(BaseModel):
    first_name: constr(min_length=2) = Field(...)
    last_name_father: constr(min_length=2) = Field(...)
    last_name_mother: constr(min_length=2) = Field(...)
    enrollment: str = Field(...)
    grade_id: UUID = Field(...)
    school_id: UUID = Field(...)
    user_id: UUID = Field(...)

class Student(BaseModel):
    id: UUID
    first_name: str
    last_name_father: str
    last_name_mother: str
    enrollment: str
    grade_id: UUID
    school_id: UUID
    user_id: UUID

    class Config:
        orm_mode = True
