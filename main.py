from fastapi import FastAPI
from routers import user, auth
from fastapi.middleware.cors import CORSMiddleware
from core.database import Base, engine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("Server is running")

# include routers from routers folder
app.include_router(user.router)
app.include_router(auth.router)
