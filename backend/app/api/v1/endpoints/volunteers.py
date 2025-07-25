from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.volunteer import Volunteer
from app.schemas.volunteer import VolunteerCreate, VolunteerRead
from app.services.volunteer_service import create_volunteer

router = APIRouter(prefix="/volunteers", tags=["Volunteers"])

@router.post("", response_model=VolunteerRead, status_code=status.HTTP_201_CREATED)
def register_volunteer(data: VolunteerCreate, db: Session = Depends(get_db)):
    # impedir e‑mail duplicado entre voluntários
    if db.query(Volunteer).filter(Volunteer.email == data.email).first():
        raise HTTPException(status_code=400, detail="E‑mail já cadastrado.")
    # impedir duplicado também em organizações
    from app.db.models.organization import Organization
    if db.query(Organization).filter(Organization.email == data.email).first():
        raise HTTPException(status_code=400, detail="E‑mail em uso por organização.")
    return create_volunteer(db, data)
