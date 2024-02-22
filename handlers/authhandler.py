from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from jose import jwt
from datetime import timedelta
from utils.envutils import Environment


env=Environment()
SECRET_KEY = env.secret_key
ALGORITHM = env.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = env.access_token_expire_minutes
TOKEN_TYPE = env.TOKEN_TYPE
TOKEN_KEY = env.TOKEN_KEY

class AuthHandler:
    # check fot the user credentials(yet ot implement the database)
    def login(request: OAuth2PasswordRequestForm = Depends()):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = jwt_token.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )

        response = JSONResponse(
            content={"access_token": access_token, "token_type": TOKEN_TYPE}
        )

        response.set_cookie(key=TOKEN_KEY, value=access_token,
                            expires=access_token_expires.total_seconds())

        return response
    # return {"message": "Invalid credentials"}

    def logout():
        # Logout logic
        return "Logged out successfully"
