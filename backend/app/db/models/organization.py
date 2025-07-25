# app/db/models/organization.py
from sqlalchemy import Column, String
from app.db.models.base_user import BaseUser

class Organization(BaseUser):
    __tablename__ = "organizations"

    org_name = Column(String(255), nullable=False)
    # campos extras: website, phone, etc.