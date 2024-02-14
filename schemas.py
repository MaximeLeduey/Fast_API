from pydantic import BaseModel
from sqlalchemy import  Date


class ArticleBase(BaseModel):
    title: str
    content : str 
    


class ArticleCreate(ArticleBase):
    # id: int
    publication_date : Date