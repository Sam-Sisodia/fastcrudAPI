from fastapi import FastAPI,Depends,status ,responses,Response
from sqlalchemy.orm import Session
from models import Blog
from database import engine,SessionLocal
from schemas import Blog
import models
import schemas



models.Base.metadata.create_all(engine)


app = FastAPI()
 

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()  


#get single
@app.get("/blog/{id}" ,status_code=200)
def get_one(id:int,response:Response, db: Session=Depends(get_db)):
    single_data = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not single_data:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'msg': f"Blog with this id {id} is not found"}
    return  single_data


#delete

@app.delete("/blog/{id}" , status_code =status.HTTP_404_NOT_FOUND)
def blog_delete(id:int , db: Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"
    




@app.put("/blog/{id}" , status_code =status.HTTP_202_ACCEPTED)
def update_data(id:int ,request:schemas.Blog , db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        return {'msg' :"post not found"}

   # blog.update({'title': request.title, 'body': request.body})

    blog.update(request.dict())
 
    db.commit()
    return "Updated Successfully"



@app.post("/blog/", status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog , db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.get("/blog")
def get_all( db: Session=Depends(get_db)):
    all_data = db.query(models.Blog).all()
    return all_data 






