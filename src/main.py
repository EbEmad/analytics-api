from contextlib import asynccontextmanager
from typing import Union
from api.events import router as events_router
from fastapi import FastAPI
from pydantic import BaseModel

from api.db.session import init_db
# /api/events

products_db=[
    {'id':1,'name':'product 1','price':100},
    {'id':2,'name':'product 2','price':200},
    {'id':3,'name':'product 3','price':300},
    {'id':4,'name':'product 4','price':400},
    {'id':5,'name':'product 5','price':500},
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/healthz")
def read_root():
    return {"Message": "weclome to the ecommerece API"}

app.include_router(events_router,prefix="/api/events")

@app.get("/products")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"products": products_db}

class Product(BaseModel):
    id: int
    name: str
    price: float


@app.post("/products")
async def add_product(obj:Product):
    name="anas"
    price="1000"
    id=6
    products_db.append({'id':id,'name':name,'price':price})
    
    return {"messge":"product added successfully","product": obj}


@app.get("/Anas")  # THIS IS use as endpoint
async def read_root():
    return {"Hello": "World Eng Anas"}