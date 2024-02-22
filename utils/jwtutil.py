#! Not sure if it works or not jfix the code if it doesn't work
from fastapi import Request, Response, HTTPException, status
from fastapi import HTTPException, status, Request, Response
from jose import JWTError, jwt
from datetime import datetime, timedelta
from models import schemas
import os
from utils.envutils import Environment

env = Environment()
secret_key = env.secret_key
ALGORITHM = env.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = env.access_token_expire_minutes
TOKEN_TYPE = env.TOKEN_TYPE
TOKEN_KEY = env.TOKEN_KEY

# Create the access token


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_token(req: Request, res: Response):
    try:
        token = await req.cookies.get("token")

        if token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials: Token missing",
                headers={"WWW-Authenticate": "Bearer"},
            )

        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials: 'sub' claim missing",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token_data = schemas.TokenData(email=email)
        # req.state.token_data = token_data  # Store the token_data in the request state
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return res
