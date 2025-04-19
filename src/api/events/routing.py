from fastapi import APIRouter
from .schemas import (
    EventSchema, 
    EventlistSchema, 
    EventCreateSchema,
    EventUpdateSchema

)
router=APIRouter()


# list view
# GET /api/events
@router.get("/")
def read_events()-> EventlistSchema:
    # a bunch of items in a table
    return {
        "results": [{'id':1},{'id':2}] ,
        "count": 2
    }

# send data to the server
# POST /api/events
# create view
@router.post("/")
def create_events(payload:EventCreateSchema)-> EventSchema:
    # a bunch of items in a table
    print(payload)
    print(type(payload))
    return {'id':5555}

# update this data
# PUT /api/events/id
@router.put("/{event_id}")
def update_events(event_id:int,payload:EventUpdateSchema)-> EventlistSchema:
    # a bunch of items in a table
    print(payload)
    print(type(payload))
    return {
        "results": [{'id':1},{'id':2}] ,
        "count": 2
    }

# @router.delete("/{event_id}")
# def delete_events(event_id:int,payload:dict={})-> EventlistSchema:
#     # a bunch of items in a table
#     return {
#         "results": [{'id':1},{'id':2}] ,
#         "count": 2
#     }


# get /spi/events/id
@router.get("/{event_id}")
def get_events(event_id:int)->EventSchema:

    # a single row
    return {
        "id": event_id
    }



