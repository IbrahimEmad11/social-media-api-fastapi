from fastapi import FastAPI, Response, status, HTTPException ,Depends
from fastapi.params import Body
from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from time import sleep
from dotenv import load_dotenv
import os
from . import models,schemas
from .database import engine ,get_db
from .routers import user, post, auth

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

models.Base.metadata.create_all(bind=engine)



app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database Connected Successfully!")
        break
    
    except Exception as err:
        print("Database Connection failed, Error:", err)
        sleep(3)
        

# all_posts = [
#     {
#         "title": "my 1st post",
#         "content": "This is my first post",
#         "published": False,
#         "id": 1
#     }
# ]

# def find_post(id):
#     for p in all_posts:
#         if p["id"] == id:
#             return p

# def find_index(id):
#     for i, p in enumerate(all_posts):
#         if p["id"] == id:
#             return i

# @app.get("/alchemy")
# def test_alchemy(db: Session = Depends(get_db)):
#     posts= db.query(models.Posts).all()
#     return {"test":posts}

@app.get('/')
def root():
    return {"message": "Hello World"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)




