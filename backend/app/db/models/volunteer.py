# app/db/models/volunteer.py
from sqlalchemy import Column, String
from app.db.models.base_user import BaseUser

class Volunteer(BaseUser):
    __tablename__ = "volunteers"

    full_name = Column(String(255), nullable=False)
    # campos extras, se quiser: skills, availability, etc.