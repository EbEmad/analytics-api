# api/events/routing.py
from fastapi import APIRouter
from .schemas import EventSchema,EventListSchema
router = APIRouter()

@router.get("/")
def create_event()->EventListSchema:
    return {"items": [{'id':1},{'id': 2},{'id': 3}]}


@router.post("/")
def read_event(dct:dict={})->EventSchema:
    print(dct)
    return {
        "id": 123
        }



@router.get("/{event_id}")
def get_event(event_id:int)->EventSchema:
    return {"id":event_id}