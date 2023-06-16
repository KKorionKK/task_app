from pydantic import BaseModel
from datetime import datetime

class ItemSchema(BaseModel):
    header: str
    description: str
    status: bool
    created: datetime
    deadline: datetime

class ItemUpdateSchema(BaseModel):
    id: int
    header: str
    description: str
    status: bool
    deadline: datetime