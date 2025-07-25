from pydantic import BaseModel, EmailStr, constr

class VolunteerBase(BaseModel):
    email: EmailStr
    full_name: constr(min_length=2, max_length=255)

class VolunteerCreate(VolunteerBase):
    password: constr(min_length=8)

class VolunteerRead(VolunteerBase):
    id: int
    class Config:
        orm_mode = True