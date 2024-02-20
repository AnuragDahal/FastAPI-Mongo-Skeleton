from models import schemas


async def CREATE_USER(request: schemas.User):
    """
    Insert a new student record.
    A unique `id` will be created and provided in the response.
    """
    new_user = await request.insert_one(
        request.dict(by_alias=True, exclude={"id"})
    )
    return new_user


async def READ_USER():

    return {"message": "User data returned successfully."}
