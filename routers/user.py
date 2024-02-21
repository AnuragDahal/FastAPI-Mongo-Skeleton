from fastapi import APIRouter, status, HTTPException
from handlers.userhandler import (
    CREATE_USER,
    READ_USER,
    # UPDATE_USER,
)
from typing import List
from handlers.exception import (
    ErrorHandler,
    NotFoundHandler,
    UnauthorizedHandler,
    ForbiddenHandler,
    ServerErrorHandler,
)
from models import schemas
router = APIRouter(tags=["user"])


@router.post("/user", status_code=status.HTTP_201_CREATED,)
async def create_user(req: schemas.User):
    try:
        user = CREATE_USER(req)
        return user

    except Exception as e:
        return ErrorHandler(e)


@router.get("/user", response_model=List[schemas.User], status_code=status.HTTP_200_OK,)
async def read_user():

    user = READ_USER()
    return user


# @router.patch("/user/{email}", response_model=schemas.User)
# async def update_user(email: str):

#     update_data = UPDATE_USER(email)
#     return update_data
