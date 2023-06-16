from fastapi import APIRouter, Depends, HTTPException, status
from .authorization import get_current_active_user
from typing import Annotated, List
from ..models.user_model import User

from sqlalchemy.orm import Session
from ..database import Base, engine, SessionLocal

from ..internal.crud_items import crud_get_all_items, crud_create_item, crud_delete_item, crud_update_item
from ..schemas.item_schema import ItemSchema, ItemUpdateSchema

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

items_router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {'description': 'Not Found'}},
)

@items_router.get('/')
async def get_all_items(current_user: Annotated[User, Depends(get_current_active_user)], skip: int = 0,
                   limit: int = 100, db: Session = Depends(get_db)):
    if current_user:
        items = crud_get_all_items(db=db, user=current_user.id, skip=skip, limit=limit)
        return items
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authenticated",
            headers={"WWW-Authentication": "Bearer"}
        )

@items_router.post('/create_item')
async def create_item(current_user: Annotated[User, Depends(get_current_active_user)],
                 item: ItemSchema, db: Session = Depends(get_db)):
    if current_user:
        response = crud_create_item(
            db=db,
            header=item.header,
            description=item.description,
            status=item.status,
            user_id=current_user.id,
            created=item.created,
            deadline=item.deadline
        )
        return response
    

@items_router.post('/delete_item/{item_id}')
async def delete_item(current_user: Annotated[User, Depends(get_current_active_user)], item_id: int, db: Session = Depends(get_db)):
    return crud_delete_item(db=db, item_id=item_id)

@items_router.put('/update_item/')
async def update_item(current_user: Annotated[User, Depends(get_current_active_user)], item: ItemUpdateSchema, db: Session = Depends(get_db)):
    response =crud_update_item(db=db, item=item)
    return response
