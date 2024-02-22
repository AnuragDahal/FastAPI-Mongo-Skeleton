from models import schemas
from core.database import user_collection
from handlers.exception import ErrorHandler


class Validate:
    @staticmethod
    def verify_email(email: str):
        check_email_length = user_collection.find_one({"email": email})
        if check_email_length:
            return email
        raise ErrorHandler.NotFound("Email not found")


class UserManager:
    @staticmethod
    def create(request: schemas.User):
        """
        Insert a new student record.
        A unique `id` will be created and provided in the response.
        """
        new_user = user_collection.insert_one(request.model_dump(exclude=None))
        if new_user.inserted_id:
            return ErrorHandler.ALreadyExists("User already exists")
        return {"id": str(new_user.inserted_id)}

    @staticmethod
    def read():
        """
        Retrieve all student records.
        """
        count = user_collection.count_documents({})
        if count > 0:
            users = user_collection.find()
            return users
        raise ErrorHandler.NotFound("No user found")

    @staticmethod
    def update(old_email: str, request: schemas.UpdateUserEmail):
        """
        Update a student record.
        """
        user = user_collection.find_one_and_update(
            {"email": old_email}, {"$set": request.model_dump(exclude=None)})
        return user

    @staticmethod
    def delete(email: str):
        """
        Delete a student record.
        """
        user = user_collection.delete_one({"email": email})
        if user.deleted_count == 0:
            raise ErrorHandler.NotFound("User not found")
        return {"message": "User deleted successfully"}
