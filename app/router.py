from fastapi import APIRouter,HTTPException,Path,Depends
from config import SessionLocal

from sqlalchemy.orm import Session
from schemas import BookSchema,RequestBook,Response

import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

    
@router.post('create')
async def create(request:RequestBook, db:Session = Depends(get_db)):
    crud.create_book(db,request.parameter)
    return Response(code=200 , status="ok", message="Book created Sucessfull").dict(exclude_none=True)


@router.get("/")
async def get(db:Session= Depends(get_db)):
    _book = crud.get_book(db,0,100)
    return Response(code=200 , status="ok", message="Sucess Fatch All data ", result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int, db:Session= Depends(get_db)):
    _book = crud.get_book_by_id(db,id)
    return Response(code=200 , status="ok", message="Sucess get data ", result=_book).dict(exclude_none=True)


@router.post("/update")
async def update_book(request:RequestBook, db:Session= Depends(get_db) ):
    _book = crud.update_book(db,book_id=request.parameter.id,
                title=request.parameter.title, dis = request.parameter.dis)
    return Response(code=200 , status="ok", message="Update data Success",).dict(exclude_none=True)


@router.delete("/{id}")
async def delete(id:int , db:Session= Depends(get_db)):
    crud.remove_book(db , book_id=id)
    return Response(code=200 , status="ok", message="Delete Successfully",).dict(exclude_none=True)
    