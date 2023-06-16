from sqlalchemy.orm import Session

from ..models.user_model import User

from datetime import datetime

def crud_get_user(db: Session, username: str):
    user = db.query(User).filter(User.email == username).first()
    if user:
        return user
    

def crud_create_user(db: Session, name: str, surname: str, email: str, 
                     password: str, active: bool = True, created: datetime = datetime.utcnow()):
    user = User(name = name, surname = surname, email = email, 
                password = password, active = active, created = created)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
