from fastapi import FastAPI


import models
from config import engine

models.Base.metadata.create_all(bind=engine)

import router
app  = FastAPI()



@app.get('/')
async def Home():
    return "Hello Sajal"

app.include_router(router.router,prefix="/books", tags=['books'])
