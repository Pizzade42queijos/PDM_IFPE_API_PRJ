# app/db/models/base_user.py
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class BaseUser(Base):
    __abstract__ = True          # não cria tabela ― só herança
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)