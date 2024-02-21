from fastapi import APIRouter, status
from handlers.userhandler import ManageUser
from handlers.exception import ErrorHandler
from typing import List
from handlers.exception import Error
from models import schemas
router = APIRouter(tags=["user"])


@router.post("/user", status_code=status.HTTP_201_CREATED,)
async def create_user(req: schemas.User):
    
        user = ManageUser.create(req)
        return user


@router.get("/user", response_model=List[schemas.User], status_code=status.HTTP_200_OK,)
async def read_user():

    user = READ_USER()
    return user


@router.patch("/update/{old_email}", response_model=schemas.User)
async def update_user(old_email: str, request: schemas.UpdateUserEmail):

    update_data = UPDATE_USER(old_email, request)
    return update_data
