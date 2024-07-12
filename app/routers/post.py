from fastapi import FastAPI, Response, status, HTTPException ,Depends, APIRouter
from typing import List , Optional
from sqlalchemy.orm import Session 
from .. import models, schemas , oauth2
from ..database import engine ,get_db

router = APIRouter(
    prefix= "/posts",
    tags=["Posts"]
)


@router.get("/", response_model= List[schemas.PostResponse] )
def get_posts(db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user), limit: int = 10 , skip : int = 0 , search : Optional[str] = "" ):

    # cursor.execute(""" SELECT * from posts """)
    # posts = cursor.fetchall()

    posts = db.query(models.Posts).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()

 

    return posts

@router.get("/profile", response_model= List[schemas.PostResponse] )
def get_my_posts(db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user), limit: int = 10 , skip : int = 0 , search : Optional[str] = ""):

    # cursor.execute(""" SELECT * from posts """)
    # posts = cursor.fetchall()

    my_posts = db.query(models.Posts).filter(models.Posts.user_id == curr_user.id).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()


    return my_posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate , db: Session = Depends(get_db) , curr_user : int = Depends(oauth2.get_current_user)):

    # cursor.execute(""" INSERT INTO posts (title ,content ,published) VALUES (%s , %s, %s) RETURNING * """ ,(post.title, post.content ,post.published))
    # created_post = cursor.fetchone()
    # conn.commit()

    print(curr_user.email)
    created_post = models.Posts(user_id = curr_user.id,**post.model_dump())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)

    return created_post

@router.get("/{id}",response_model= schemas.PostResponse)
def get_post(id: int,db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user)):

    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} isn't found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user)):

    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """,(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Posts).filter(models.Posts.id== id)
    deleted_post = post_query.first()
    
    if deleted_post is None:
        raise HTTPException(detail=f"Post with id {id} doesn't exist", status_code=status.HTTP_404_NOT_FOUND)
    
    if deleted_post.user_id != curr_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform this action")
 
    post_query.delete(synchronize_session = False) 
    db.commit()

    return {Response(status_code=status.HTTP_204_NO_CONTENT)}

@router.put('/{id}', response_model= schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate,db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user) ) :

    # cursor.execute(""" UPDATE posts SET title = %s , content = %s , published = %s WHERE id = %s RETURNING * """,(post.title , post.content , post.published,str(id),))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    updated_post = post_query.first()

    if updated_post is None:
        raise HTTPException(detail=f"Post with id {id} doesn't exist", status_code=status.HTTP_404_NOT_FOUND)
    
    if updated_post.user_id != curr_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform this action")

    post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()

    return post_query.first()