from fastapi import APIRouter
from handlers.userhandler import (
    CREATE_USER,


)
router = APIRouter(tags=["user"])


@router.get("/user")
async def create_user():
    try:
        user = CREATE_USER()
        return user
    except Exception as e:
        return {"error": str(e)}
