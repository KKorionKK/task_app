from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from ..models.user_model import User
from .authorization import get_current_active_user

users_router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not Found'}},
)

@users_router.get("/me/")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

