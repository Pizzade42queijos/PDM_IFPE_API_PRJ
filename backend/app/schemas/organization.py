from pydantic import BaseModel, EmailStr, constr

class OrganizationBase(BaseModel):
    email: EmailStr
    org_name: constr(min_length=2, max_length=255)

class OrganizationCreate(OrganizationBase):
    password: constr(min_length=8)

class OrganizationRead(OrganizationBase):
    id: int
    class Config:
        orm_mode = True
