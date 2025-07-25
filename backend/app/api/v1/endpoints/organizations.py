from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationRead
from app.services.organization_service import create_organization
from app.db.models.volunteer import Volunteer

router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.post("", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
def register_org(data: OrganizationCreate, db: Session = Depends(get_db)):
    # checa duplicidade em ambas as tabelas
    if db.query(Organization).filter(Organization.email == data.email).first() \
       or db.query(Volunteer).filter(Volunteer.email == data.email).first():
        raise HTTPException(status_code=400, detail="E‑mail já cadastrado.")
    return create_organization(db, data)
