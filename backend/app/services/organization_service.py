from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.db.models.organization import Organization
from app.schemas.organization import OrganizationCreate

_pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _hash(pwd: str) -> str:
    return _pwd.hash(pwd)

def create_organization(db: Session, data: OrganizationCreate) -> Organization:
    o = Organization(
        email=data.email,
        hashed_password=_hash(data.password),
        org_name=data.org_name,
    )
    db.add(o)
    db.commit()
    db.refresh(o)
    return o
