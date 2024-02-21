from models import schemas
from core.database import user_collection
from handlers.exception import (
    ErrorHandler,
    NotFoundHandler,
    UnauthorizedHandler,
    ForbiddenHandler,
    ServerErrorHandler,
)


def CREATE_USER(request: schemas.User):
    """
    Insert a new student record.
    A unique `id` will be created and provided in the response.
    """
    new_user = user_collection.insert_one(request.model_dump(exclude=None))
    return {"id": str(new_user.inserted_id)}


def READ_USER():
    """
    Retrieve all student records.
    """
    count = user_collection.count_documents({})
    if count > 0:
        users = user_collection.find()
        return users
    raise NotFoundHandler("No user found")
