from fastapi import APIRouter
from handlers.userhandler import READ_USER
router = APIRouter(tags=["user"])


@router.get("/user")
async def read_user():
    try:
        user = READ_USER()
        return user
    except Exception as e:
        return {"error": str(e)}
