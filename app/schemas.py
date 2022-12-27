from  typing import List,Optional,Generic,TypeVar
from pydantic import BaseModel, Field

from pydantic.generics import GenericModel

T = TypeVar('T')

class BookSchema(BaseModel):
    id: Optional[int] = None
    title : Optional[str] = None
    title : Optional[str] = None

    class config:
        orm_model = True



class RequestBook(BaseModel):
    parameter : BookSchema= Field(...)
      


class Response(GenericModel,Generic[T]):
    code :str
    status :str
    message :str
    result :Optional[T]