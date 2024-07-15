import pydantic
from pydantic import BaseModel , EmailStr, conint
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    email : EmailStr
    id:int
    created_at : datetime

    class Config:
        from_attributes = True

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

    post_owner : UserResponse

    class Config:
        from_attributes = True

class PostVote(BaseModel):
    Posts:PostResponse
    votes:int

    class Config:
        from_attributes = True


class Token(BaseModel):
    token : str
    token_type : str 

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id : int
    dir: conint(ge=0,le=1)