from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    active: bool
    created: datetime
