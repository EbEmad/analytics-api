# api/events/routing.py
from fastapi import APIRouter
import os
from .schemas import EventSchema,EventListSchema,EventCreateSchema,EventUpdateSchema
router = APIRouter()

@router.post("/")
def create_event(payload:EventCreateSchema)->EventListSchema:
    data=payload.model_dump()
    return {"items": [{'id':1},{'id': 2},{'id': 3}],**data}

@router.get("/")
def read_event()->EventListSchema:
    print(os.environ.get("DATABASE_URL"))
    return {"items": [{'id':1},{'id': 2},{'id': 3}]}


# @router.post("/")
# def read_event(payload:EventCreateSchema)->EventSchema:
#     print(payload.page)
#     return {
#         "id": 123,
#         "page":payload.page
#         }



@router.get("/{event_id}")
def get_event(event_id:int)->EventSchema:
    return {"id":event_id}



@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema)->EventSchema:
    data=payload.model_dump()
    return {"id":event_id,**data}


# @router.delete("/{event_id}")
# def update_event(event_id:int,payload:dict={})->EventSchema:
#     return {"id":event_id}