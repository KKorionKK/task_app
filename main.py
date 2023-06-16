from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.routers.authorization import auth_router
from backend.routers.users import users_router
from backend.routers.items import items_router

app = FastAPI()

origins = [
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
    )

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(items_router)

@app.get("/")
def main():
    return {"message": "Hello!"}