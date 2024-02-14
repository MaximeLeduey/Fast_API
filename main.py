from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# class Article(BaseModel):
#     id: int
#     title: str
#     content: str
#     publication_date: Optional[datetime] = datetime.now()
    
          
# articles: List[Article] = []

# articles.append(Article(id=1, title="premier article", content="le contenu de mon premier article"))


@app.post("/create_article/")
def create_article(article: Article):
    """
    Route POST pour créer un nouvel article.
    """
 
    return {"article": article}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

