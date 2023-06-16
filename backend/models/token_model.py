from pydantic import BaseModel
from ..database import Base

class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    username: str | None = None