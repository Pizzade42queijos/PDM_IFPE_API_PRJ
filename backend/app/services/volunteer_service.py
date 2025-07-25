from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.db.models.volunteer import Volunteer
from app.schemas.volunteer import VolunteerCreate

_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _hash(pwd: str) -> str:
    return _pwd.hash(pwd)

def create_volunteer(db: Session, data: VolunteerCreate) -> Volunteer:
    v = Volunteer(
        email=data.email,
        hashed_password=_hash(data.password),
        full_name=data.full_name,
    )
    db.add(v)
    db.commit()
    db.refresh(v)
    return v
