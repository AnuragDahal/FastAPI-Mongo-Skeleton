from fastapi import APIRouter, status, Depends
from handlers.userhandler import (
    CREATE_USER,
)
from models import schemas
from core.database import get_db
router = APIRouter(tags=["user"])


@router.post("/user",status_code=status.HTTP_201_CREATED,)
async def create_user(req: schemas.User, db: get_db):
    try:
        user = CREATE_USER(req, db)
        return user
    
    except Exception as e:
        return {"error": str(e)}
