from models import schemas, models
from core.database import get_db


async def CREATE_USER(request: schemas.User, db: get_db):
    """
    Insert a new student record.
    A unique `id` will be created and provided in the response.
    """
    new_user = models.User(**request)
    new_user.save()


async def READ_USER():

    return {"message": "User data returned successfully."}
