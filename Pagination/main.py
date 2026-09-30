from fastapi import FastAPI
import json
from Schemas import Response,PaginatedResponse
from contextlib import asynccontextmanager

DATA=[]

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('---------------App started----------------------')
    global DATA
    with open("data.json", "r", encoding="utf-8") as f:
        print('-------------file read------------------')
        DATA = json.load(f)["data"]
    yield
    print('---------------App CLosed----------------------')

app = FastAPI(lifespan=lifespan)

@app.get("/search/" ,response_model=PaginatedResponse , tags=["Search"])
async def search(skip:int=0,limit:int=100):
    result=DATA[skip:skip+limit]
    total=len(DATA)
    has_more=skip + len(result) < total

    return PaginatedResponse(
        data=result,
        total=total,
        skip=skip,
        limit=limit,
        has_more=has_more
    )

        