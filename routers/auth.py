from fastapi import APIRouter
from handlers.authhandler import (
    LOGIN,
    LOGOUT

)
router = APIRouter(tags=["auth"])


@router.get("/login")
async def login():

    user_in = LOGIN()
    return user_in


@router.get("/logout")
async def logout():

    user_out = LOGOUT()
    return user_out
