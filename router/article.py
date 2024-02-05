from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from auth.oauth2 import oauth2_schema

router = APIRouter(
    prefix='/article',
    tags=['article']
)

#Create Article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session= Depends(get_db)):
    return db_article.create_article(db, request)

#get specific article
@router.get('/{id}') #, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return{
      'data' : db_article.get_article(db, id)
    }  