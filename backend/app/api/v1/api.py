from fastapi import APIRouter
from .endpoints import volunteers, organizations

router = APIRouter()
router.include_router(volunteers.router)
router.include_router(organizations.router)
