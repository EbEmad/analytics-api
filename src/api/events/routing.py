import os
from fastapi import APIRouter
from .models import (
    EventModel, 
    EventlistSchema, 
    EventCreateSchema,
    EventUpdateSchema

)
router=APIRouter()

from api.db.config import DATABASE_URL
# list view
# GET /api/events
@router.get("/")
def read_events()-> EventlistSchema:
    # a bunch of items in a table
    print(os.environ.get("DATABASE_URL"),DATABASE_URL)
    return {
        "results": [{'id':1},{'id':2}] ,
        "count": 2
    }

# send data to the server
# POST /api/events
# create view
@router.post("/")
def create_events(payload:EventCreateSchema)-> EventModel:
    # a bunch of items in a table
    print(payload.page)
    print(type(payload))
    data=payload.model_dump() # payload -> dict -> pydantic
    return  {'id':123,**data}

# update this data
# PUT /api/events/id
@router.put("/{event_id}")
def update_events(event_id:int,payload:EventUpdateSchema)-> EventModel:
    # a bunch of items in a table
    print(payload.description)
    print(type(payload))
    data=payload.model_dump() # payload -> dict -> pydantic
    return {'id':event_id,**data}

# @router.delete("/{event_id}")
# def delete_events(event_id:int,payload:dict={})-> EventlistSchema:
#     # a bunch of items in a table
#     return {
#         "results": [{'id':1},{'id':2}] ,
#         "count": 2
#     }





