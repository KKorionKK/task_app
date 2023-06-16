from sqlalchemy.orm import Session

from ..models.user_model import User
from ..models.item_model import Item

from datetime import datetime

def crud_get_all_items(db: Session, user: str, skip: int = 0, limit: int = 100):
    user_id = db.query(User).filter(User.id == user).first()
    items = db.query(Item).filter(Item.user_id == user_id.id).offset(skip).limit(limit=limit).all()
    return items

def crud_get_item_by_id(db: Session, item_id):
    item = db.query(Item).filter(Item.id == item_id).first()
    return item

def crud_create_item(db: Session, header: str, description: str, status: bool, user_id: int, created: datetime = datetime.utcnow(), deadline: datetime = None):
    item = Item(
        header = header,
        description = description,
        status = status, 
        created = created,
        deadline = deadline,
        user_id = user_id
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def crud_delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(item)
    db.commit()

    return item

def crud_update_item(db: Session, item: Item):
    _item = crud_get_item_by_id(db=db, item_id=item.id)
    if _item:
        _item.header = item.header
        _item.description = item.description
        _item.status = item.status
        _item.deadline = item.deadline
        db.commit()
        db.refresh(_item)

        return _item
    else:
        return {"message": "Not found"}