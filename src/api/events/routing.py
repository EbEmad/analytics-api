# api/events/routing.py
from fastapi import APIRouter,Depends
import os
from api.db.session import get_session
from sqlmodel import Session
from .models import EventModel,EventListSchema,EventCreateSchema,EventUpdateSchema
router = APIRouter()

@router.post("/",response_model=EventModel)
def create_event(payload:EventCreateSchema,session:Session=Depends(get_session)):
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
def get_event(event_id:int)->EventModel:
    return {"id":event_id}



@router.put("/{event_id}")
def update_event(event_id:int,payload:EventUpdateSchema)->EventModel:
    data=payload.model_dump()
    return {"id":event_id,**data}


# @router.delete("/{event_id}")
# def update_event(event_id:int,payload:dict={})->EventModel:
#     return {"id":event_id}