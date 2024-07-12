from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate (PostBase):
    pass

class PostResponse(PostBase):
    id:int
    created_at : datetime
    user_id : int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    email : EmailStr
    id:int
    created_at : datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    token : str
    token_type : str 

class TokenData(BaseModel):
    id: Optional[int] = None
