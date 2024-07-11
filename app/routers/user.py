from fastapi import  status, HTTPException ,Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas , utils
from ..database import engine ,get_db


router = APIRouter(
    prefix = "/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate , db: Session = Depends(get_db)):

    hashed_pass = utils.hash_password(user.password)
    user.password = hashed_pass
    created_user = models.User(**user.model_dump())

    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    
    return created_user

@router.get("/{id}", response_model= schemas.UserResponse)
def get_user(id: int,db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} isn't found")
    
    return user