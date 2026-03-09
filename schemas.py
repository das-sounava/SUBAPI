from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str

class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True


