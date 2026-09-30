from pydantic import BaseModel
class Response(BaseModel):
    id:int
    name:str
    email:str
    status:str

class PaginatedResponse(BaseModel):
    data:list[Response]
    total:int
    skip:int
    limit: int
    has_more:bool