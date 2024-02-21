from fastapi import APIRouter
from handlers.authhandler import AuthHandler
router = APIRouter(tags=["auth"])


@router.get("/login")
async def login():

    user_in = AuthHandler.LOGIN()
    return user_in


@router.get("/logout")
async def logout():

    user_out = AuthHandler.LOGOUT()
    return user_out
