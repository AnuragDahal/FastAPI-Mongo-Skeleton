from models import schemas
from core.database import user_collection
from handlers.exception import (
    ErrorHandler,
    NotFoundHandler,
    UnauthorizedHandler,
    ForbiddenHandler,
    ServerErrorHandler,
)

class ManageUser:
    def create(request: schemas.User):
        """
        Insert a new student record.
        A unique `id` will be created and provided in the response.
        """
        new_user = user_collection.insert_one(request.model_dump(exclude=None))
        if new_user in user_collection.find():
            return ALreadyExistsHandler("User already exists")
        return {"id": str(new_user.inserted_id)}



    def read():
        """
        Retrieve all student records.
        """
        count = user_collection.count_documents({})
        if count > 0:
            users = user_collection.find()
            return users
        raise NotFoundHandler("No user found")

    def update(old_email: str, request: schemas.UpdateUserEmail):
        """
        Update a student record.
        """
        user = user_collection.__find_and_modify({"email": old_email}, {"$set": request.model_dump(exclude=None)})
        return user
    
    def delete(email: str):
        """
        Delete a student record.
        """
        user = user_collection.delete_one({"email": email})
        if user.deleted_count == 0:
            raise NotFoundHandler("User not found")
        return {"message": "User deleted successfully"}    
    