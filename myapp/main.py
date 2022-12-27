from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {"name": "sajal"} }

@app.get("/about")
def about():
    return "This is about page" 


# fatch all blogs
@app.get("/blog/{id}")                     # id as number   def blog(id:int)
def blog(id):
    return {'data'  : {'id':id}}



#post method - create
#import base Moddel 
from pydantic import BaseModel
from typing import Optional, Union

class Blog(BaseModel):
    title: str
    body : str
    published : Optional[bool]
    




@app.post("/bolg")
def create_blog(blog:Blog):
    return {'msg': f"Created Successfully with blog {blog.title}"}