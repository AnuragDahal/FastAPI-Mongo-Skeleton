from fastapi import APIRouter, status
from handlers.userhandler import (
    CREATE_USER,
)
from core.database import db
router = APIRouter(tags=["user"])


@router.post("/user",
             status_code=status.HTTP_201_CREATED,)
async def create_user():
    try:
        user = CREATE_USER()
        return user
    except Exception as e:
        return {"error": str(e)}
