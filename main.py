from fastapi.responses import JSONResponse, PlainTextResponse
from typing import Optional
from fastapi import FastAPI, Request
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from db.database import engine
from db import models
from schemas import UserBase, UserDisplay, ArticleBase, ArticleDisplay
from exceptions import StoryException
from fastapi.exceptions import HTTPException

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc:StoryException):
   return JSONResponse(
       status_code= 418, 
       
       content= {'detail': exc.name}
   )

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400) #it covers all the exceptions thatswhy we are not using now. filter it

models.Base.metadata.create_all(engine)