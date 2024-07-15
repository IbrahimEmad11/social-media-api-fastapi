from fastapi import  status, HTTPException ,Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models, schemas , utils,database,oauth2
from ..database import engine ,get_db


router = APIRouter(
    prefix="/vote",
    tags = ["Votes"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def add_vote(vote:schemas.Vote, db : Session = Depends(database.get_db), curr_user: int =Depends(oauth2.get_current_user)): 
    
    post = db.query(models.Posts).filter(models.Posts.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == curr_user.id)
    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {curr_user.id} has already voted on post {vote.post_id}")
        
        new_vote= models.Vote(user_id = curr_user.id , post_id = vote.post_id)
        db.add(new_vote)
        db.commit()
        return {"message": "Voted Successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Vote does not exist")
        
        vote_query.delete(synchronize_session = False)
        db.commit()

        return{"message": "Deleted Successfully"}


